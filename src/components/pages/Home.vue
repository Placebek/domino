<script setup>
import Card from '../../components/UI/Card.vue'
import { ref, computed, onMounted } from 'vue'
// import { getHouses } from '../../services/houses'
const product = ref([
  {
    id: 1,
    title: 'Дом 1',
    description: 'Дом 1',
    content: 'Дом 1',
  },
  {
    id: 2,
    title: 'Дом 2',
    description: 'Дом 2',
    content: 'Дом 2',
  },
  {
    id: 3,
    title: 'Дом 3',
    description: 'Дом 3',
    content: 'Дом 3',
  },
])
// const isLoading = ref(true)

// onMounted(async () => {
//   isLoading.value = true
//   const response = await getHouses()
//   if (response) {
//     product.value = response
//     isLoading.value = false
//   } else {
//     isLoading.value = false
//   }
// })

// const filteredProducts = computed(() => {
//   return Array.isArray(product.value)
//     ? product.value.filter((post) => post.request_id === null)
//     : []
// })
</script>

<template>
  <div class="mt-[5vh]">
    <div class="text-3xl font-bold text-center">Дома</div>
    <div v-for="item in product" :key="item.id">
      <Card :articledata="item" />
    </div>
  </div>
</template>
