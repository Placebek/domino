<script setup>
import { createClient, createMicrophoneAndCameraTracks } from 'agora-rtc-sdk-ng'

const APP_ID = 'bc747df82b8b4582a576de6e4262f4b6' // Замените на ваш App ID
const TOKEN = null // Если токен не используется, оставьте null
const CHANNEL = 'test' // Название канала

let localTracks = [] // Локальные треки (видео и аудио)
let remoteUsers = {} // Объект для отслеживания подключенных пользователей
let client // Клиент для взаимодействия с Agora

const joinChannel = async () => {
  // Создаём клиент
  client = createClient({ mode: 'rtc', codec: 'vp8' })

  // Присоединяемся к каналу
  await client.join(APP_ID, CHANNEL, TOKEN)

  // Создаём потоки для микрофона и камеры
  localTracks = await createMicrophoneAndCameraTracks()

  // Воспроизводим локальный поток
  localTracks[1].play('local-stream')

  // Публикуем локальный поток
  await client.publish(localTracks)
  console.log('Локальный видеопоток опубликован!')

  // Обработка входящих потоков других участников
  client.on('user-published', async (user, mediaType) => {
    await client.subscribe(user, mediaType) // Подписываемся на поток
    console.log('Подключён поток от пользователя:', user.uid)

    if (mediaType === 'video') {
      // Воспроизводим видео другого участника
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
      // Воспроизводим аудио другого участника
      const remoteAudioTrack = user.audioTrack
      remoteAudioTrack.play()
    }

    // Сохраняем информацию о подключённом пользователе
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

const leaveChannel = async () => {
  // Останавливаем и удаляем локальные треки
  console.log('Покинули канал!')
  localTracks.forEach((track) => track.stop())
  localTracks.forEach((track) => track.close())

  // Удаляем потоки других пользователей
  const remoteStreamsContainer = document.getElementById('remote-streams')
  remoteStreamsContainer.innerHTML = ''

  // Отключаемся от канала
  await client.leave()
}
</script>

<template>
  <div class="agora-container">
    <div id="local-stream" style="width: 400px; height: 300px; background: #000">
      <!-- Место для локального видео -->
    </div>
    <div id="remote-streams" style="display: flex; gap: 10px; margin-top: 10px">
      <!-- Место для видео других участников -->
    </div>
    <div>
      <button @click="joinChannel">Присоединиться</button>
      <button @click="leaveChannel">Отключиться</button>
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
