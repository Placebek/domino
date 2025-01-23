<script>
export default {
  props: ['articledata'],
  data() {
    return {
      articleData: this.articledata,
    }
  },
}
</script>

<template>
  <div class="bg-gray-200 w-[90vw] h-[20vh] m-auto mt-[2vh] rounded-lg shadow-lg">
    <div class="text-center text-3xl font-bold mt-5">{{ articleData.title }}</div>
    <div class="text-center text-xl mt-5">{{ articleData.description }}</div>
    <div class="text-center text-xl mt-5">{{ articleData.content }}</div>
  </div>
</template>
