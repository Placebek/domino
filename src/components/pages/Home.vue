<script setup>
import { ref, computed, onMounted } from 'vue'
import { getHouses } from '../../services/houses'
const product = ref([])
const isLoading = ref(true)

onMounted(async () => {
  isLoading.value = true
  const response = await getHouses()
  if (response) {
    product.value = response
    isLoading.value = false
  } else {
    isLoading.value = false
  }
})

const filteredProducts = computed(() => {
  return Array.isArray(product.value)
    ? product.value.filter((post) => post.request_id === null)
    : []
})
</script>

<template>
  <div class="ml-[15vw] mt-[5vh]"></div>
</template>
