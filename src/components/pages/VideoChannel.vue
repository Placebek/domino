<script setup>
import { createClient, createMicrophoneAndCameraTracks } from 'agora-rtc-sdk-ng'

const APP_ID = 'bc747df82b8b4582a576de6e4262f4b6' // Замените на ваш App ID
const TOKEN = null // Если токен не используется, оставьте null
const CHANNEL = 'test' // Название канала

let localTracks = [] // Локальные треки (видео и аудио)
let remoteUsers = {} // Объект для отслеживания подключенных пользователей
let client // Клиент для взаимодействия с Agora
let cameraMode = 'user' // Режим камеры: 'user' (фронтальная) или 'environment' (задняя)

// Присоединение к каналу
const joinChannel = async () => {
  client = createClient({ mode: 'rtc', codec: 'vp8' })

  await client.join(APP_ID, CHANNEL, TOKEN)

  localTracks = await createMicrophoneAndCameraTracks({}, { facingMode: cameraMode })

  // Воспроизводим локальный поток
  localTracks[1].play('local-stream')

  // Публикуем локальный поток
  await client.publish(localTracks)
  console.log('Локальный видеопоток опубликован!')

  // Подключение других участников
  client.on('user-published', async (user, mediaType) => {
    await client.subscribe(user, mediaType)
    console.log('Подключён поток от пользователя:', user.uid)

    if (mediaType === 'video') {
      const remoteVideoTrack = user.videoTrack
      const playerContainer = document.createElement('div')
      playerContainer.id = `user-${user.uid}`
      playerContainer.style.width = '400px'
      playerContainer.style.height = '300px'
      playerContainer.style.background = '#000'
      document.getElementById('remote-streams').appendChild(playerContainer)
      remoteVideoTrack.play(playerContainer)
    }

    if (mediaType === 'audio') {
      const remoteAudioTrack = user.audioTrack
      remoteAudioTrack.play()
    }

    remoteUsers[user.uid] = user
  })

  // Обработка отключения пользователей
  client.on('user-unpublished', (user) => {
    console.log('Пользователь отключился:', user.uid)
    const playerContainer = document.getElementById(`user-${user.uid}`)
    if (playerContainer) playerContainer.remove()
    delete remoteUsers[user.uid]
  })
}

// Отключение от канала
const leaveChannel = async () => {
  localTracks.forEach((track) => track.stop())
  localTracks.forEach((track) => track.close())
  document.getElementById('remote-streams').innerHTML = ''
  await client.leave()
  console.log('Покинули канал!')
}

// Переключение камеры
const switchCamera = async () => {
  cameraMode = cameraMode === 'user' ? 'environment' : 'user'
  const [audioTrack] = localTracks
  const [videoTrack] = await createMicrophoneAndCameraTracks({}, { facingMode: cameraMode })
  await client.unpublish(localTracks)
  localTracks = [audioTrack, videoTrack]
  videoTrack.play('local-stream')
  await client.publish(localTracks)
  console.log(`Камера переключена на ${cameraMode === 'user' ? 'фронтальную' : 'заднюю'}`)
}
</script>

<template>
  <div class="agora-container">
    <div id="local-stream" style="width: 400px; height: 300px; background: #000">
      <!-- Локальное видео -->
    </div>
    <div id="remote-streams" style="display: flex; gap: 10px; margin-top: 10px">
      <!-- Видео других участников -->
    </div>
    <div>
      <button @click="joinChannel">Присоединиться</button>
      <button @click="leaveChannel">Отключиться</button>
      <button @click="switchCamera">Переключить камеру</button>
    </div>
  </div>
</template>

<style>
.agora-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
</style>
