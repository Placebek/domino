<script setup>
import { createClient, createMicrophoneAndCameraTracks } from 'agora-rtc-sdk-ng'
import { useRouter } from 'vue-router';

const APP_ID = 'bc747df82b8b4582a576de6e4262f4b6' // Замените на ваш App ID
const TOKEN = null // Если токен не используется, оставьте null
const CHANNEL = 'test' // Название канала

let localTracks = [] // Локальные треки (видео и аудио)
let remoteUsers = {} // Объект для отслеживания подключенных пользователей
let client // Клиент для взаимодействия с Agora
let cameraMode = 'user' // Режим камеры: 'user' (фронтальная) или 'environment' (задняя)
const router = useRouter();

// Функция для воспроизведения звука
const playRingtone = () => {
  const audio = new Audio('D:\\Hackaton\\domino\\domino_vue\\src\\assets\\tulula-remix_01.mp3'); // Путь к звуковому файлу
  audio.play().catch(error => {
    console.error('Ошибка воспроизведения звука:', error);
  });
};

// Присоединение к каналу
const joinChannel = async () => {
  // Воспроизводим гудок
  playRingtone();

  client = createClient({ mode: 'rtc', codec: 'vp8' });

  await client.join(APP_ID, CHANNEL, TOKEN);

  localTracks = await createMicrophoneAndCameraTracks({}, { facingMode: cameraMode });

  // Воспроизводим локальный поток
  localTracks[1].play('local-stream');

  // Публикуем локальный поток
  await client.publish(localTracks);
  console.log('Локальный видеопоток опубликован!');

  // Подключение других участников
  client.on('user-published', async (user, mediaType) => {
    await client.subscribe(user, mediaType);
    console.log('Подключён поток от пользователя:', user.uid);

    if (mediaType === 'video') {
      const remoteVideoTrack = user.videoTrack;
      const playerContainer = document.createElement('div');
      playerContainer.id = `user-${user.uid}`;
      playerContainer.classList.add('remote-video');
      document.getElementById('remote-streams').appendChild(playerContainer);
      remoteVideoTrack.play(playerContainer);
    }

    if (mediaType === 'audio') {
      const remoteAudioTrack = user.audioTrack;
      remoteAudioTrack.play();
    }

    remoteUsers[user.uid] = user;
  });

  // Обработка отключения пользователей
  client.on('user-unpublished', (user) => {
    console.log('Пользователь отключился:', user.uid);
    const playerContainer = document.getElementById(`user-${user.uid}`);
    if (playerContainer) playerContainer.remove();
    delete remoteUsers[user.uid];
  });
};

// Отключение от канала
const leaveChannel = async () => {
  if (localTracks) {
    localTracks.forEach(track => {
      track.stop();
      track.close();
    });
    localTracks = [];
  }

  document.getElementById('remote-streams').innerHTML = '';

  if (client) {
    await client.leave();
    console.log('Покинули канал!');
  }
  router.push(`/`);


  client = null;
};

// Переключение камеры
const switchCamera = async () => {
  cameraMode = cameraMode === 'user' ? 'environment' : 'user';
  const [audioTrack] = localTracks;
  const [videoTrack] = await createMicrophoneAndCameraTracks({}, { facingMode: cameraMode });
  await client.unpublish(localTracks);
  localTracks = [audioTrack, videoTrack];
  videoTrack.play('local-stream');
  await client.publish(localTracks);
  console.log(`Камера переключена на ${cameraMode === 'user' ? 'фронтальную' : 'заднюю'}`);
};
</script>

<template>
  <div class="agora-container">
    <div id="remote-streams" class="fullscreen-video">
      <!-- Видео других участников -->
    </div>
    <div id="local-stream" class="local-video">
      <!-- Локальное видео -->
    </div>
    <div class="controls">
      <button @click="joinChannel" class="control-button join-button">
        <i class="fas fa-phone"></i>
      </button>
      <button @click="leaveChannel" class="control-button leave-button">
        <i class="fas fa-phone-slash"></i>
      </button>
      <button @click="switchCamera" class="control-button switch-button">
        <i class="fas fa-sync-alt"></i>
      </button>
    </div>
  </div>
</template>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

.agora-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  background: #000;
}

.fullscreen-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.local-video {
  position: absolute;
  bottom: 20px;
  right: 20px;
  width: 200px;
  height: 150px;
  z-index: 2;
  border: 2px solid #fff;
  border-radius: 10px;
  overflow: hidden;
}

.controls {
  position: absolute;
  bottom: 20px;
  left: 20px;
  z-index: 3;
  display: flex;
  gap: 10px;
}

.controls button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
}

.controls button:hover {
  background: #0056b3;
}

.remote-video {
  width: 100%;
  height: 100%;
  background: #000;
}


.join-button {
  background-color: #28a745; /* Зеленый */
}

.join-button:hover {
  background-color: #218838;
}

.leave-button {
  background-color: #dc3545; /* Красный */
}

.leave-button:hover {
  background-color: #c82333;
}

.switch-button {
  background-color: #007bff; /* Синий */
}

.switch-button:hover {
  background-color: #0056b3;
}
</style>