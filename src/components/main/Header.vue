<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '../../stores/auth.store'

const authStore = useAuthStore()
</script>

<template>
  <div class="bg-blue-700 h-[5vh] w-full relative">
    <div
      class="text-white text-[2vh] font-semibold ml-[3vw] cursor-pointer hover:text-gray-300 flex items-center absolute mt-2"
    >
      Domino
    </div>
    <div class="flex justify-end gap-x-5 mr-[2vw]">
      <a
        @click="authStore.logout()"
        class="font-bold text-[1.3vw] mt-1 text-white hover:text-gray-200 cursor-pointer"
        >Выйти</a
      >
    </div>
    <div>
      <RouterView />
    </div>
  </div>
</template>
