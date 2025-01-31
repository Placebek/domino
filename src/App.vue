<script setup>
import { useRoute } from 'vue-router'
import NavMenu from './components/main/NavMenu.vue'

const route = useRoute()
</script>

<template>
  <div class="min-h-screen">
    <!-- Условный рендеринг NavMenu -->
    <NavMenu v-if="!['/login', '/register', '/video'].includes(route.path)" />
    <router-view :key="route.path" />
  </div>
</template>
