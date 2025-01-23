<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '../../stores/auth.store'

const authStore = useAuthStore()
</script>

<template>
  <div class="bg-black w-full h-[7vh] text-white text-center font-semibold pt-3 mt-auto">
    <div>
      <RouterView />
    </div>
  </div>
</template>
