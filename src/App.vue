<script setup>
import { useRoute } from 'vue-router'
import NavMenu from './components/main/NavMenu.vue'

const route = useRoute()
</script>

<template>
  <div class="min-h-screen">
    <!-- Условный рендеринг NavMenu -->
    <NavMenu v-if="!['/login', '/register'].includes(route.path)" />
    <router-view />
    <!-- Контент маршрута -->
  </div>
</template>
