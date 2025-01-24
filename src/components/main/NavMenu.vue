<!-- eslint-disable no-unused-vars -->
<template>
  <div class="fixed bottom-0 w-full h-[7vh] z-50">
    <!-- Создаем дугу -->
    <div class="arc-menu bg-blue-200 relative">
      <div
        class="flex items-center justify-center absolute inset-x-0 top-1/2 transform -translate-y-1/2"
      >
        <RouterLink to="/home">
          <DominoHomeSVG customClass="w-[11vw] h-[5vh]" strokeWidthCustom="3" />
        </RouterLink>
      </div>
      <div class="absolute right-[10vw] mt-[1.5vh]">
        <RouterLink to="/profile">
          <UserProfileSVG customClass="w-[11vw] h-[5vh]" />
        </RouterLink>
      </div>
    </div>
  </div>
  <div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '../../stores/auth.store.js'
import DominoHomeSVG from '../UI/svg/DominoHomeSVG.vue'
import UserProfileSVG from '../UI/svg/UserProfileSVG.vue'
// eslint-disable-next-line no-unused-vars
const authStore = useAuthStore()
</script>

<style scoped>
.arc-menu {
  width: 100%; /* Полная ширина */
  height: 100%; /* Высота контейнера */
  border-top-left-radius: 20px; /* Закругление слева */
  border-top-right-radius: 20px; /* Закругление справа */
  height: 8vh; /* Высота дуги */
  clip-path: ellipse(100% 100% at 50% 100%); /* Формируем дугу */
  position: relative;
  overflow: hidden; /* Скрываем элементы за пределами дуги */
  box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2); /* Тень снизу */
}

.arc-menu .router-link {
  color: white;
}
</style>
