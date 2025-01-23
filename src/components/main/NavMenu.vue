<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '../../stores/auth.store.js'
import DominoHomeSVG from '../UI/svg/DominoHomeSVG.vue'
const authStore = useAuthStore()
</script>

<script>
export default {
  components: {
    DominoHomeSVG,
  },
}
</script>

<template>
  <div class="bg-blue-200 h-[5vh] w-full fixed bottom-0 z-50">
    <div
      class="text-white text-[2vh] font-semibold ml-[3vw] cursor-pointer hover:text-gray-300 flex items-center absolute mt-2"
    >
      <RouterLink to="/home">
        <DominoHomeSVG customClass="w-[12vw] h-[4vh]" />
      </RouterLink>
      <div class="ml-2">Дома</div>
    </div>
    <!-- <div class="flex justify-end gap-x-5 mr-[2vw]">
      <a
        @click="authStore.logout()"
        class="font-bold text-[1.3vw] mt-1 text-white hover:text-gray-200 cursor-pointer"
        >Выйти</a
      >
    </div> -->
  </div>
  <div>
    <RouterView />
  </div>
</template>
