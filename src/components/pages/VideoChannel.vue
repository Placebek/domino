<script setup>
import { createClient, createMicrophoneAndCameraTracks } from 'agora-rtc-sdk-ng'

const APP_ID = 'bc747df82b8b4582a576de6e4262f4b6' // Замените на ваш App ID
const TOKEN = null // Если токен не используется, оставьте null
const CHANNEL = 'test' // Название канала

let localTracks = []
let client

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
  console.log('Видеопоток опубликован!')
}

const leaveChannel = async () => {
  // Останавливаем и удаляем локальные треки
  console.log('Покинули канал!')
  localTracks.forEach((track) => track.stop())
  localTracks.forEach((track) => track.close())

  // Отключаемся от канала
  await client.leave()
}
</script>

<template>
  <div class="agora-container">
    <div id="local-stream" style="width: 400px; height: 300px; background: #000"></div>
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
