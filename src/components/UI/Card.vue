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
  <div class="bg-white w-[80vw] h-[80vh] m-auto mt-[10vh] rounded-lg shadow-lg">
    <div class="text-center text-3xl font-bold mt-5">{{ articleData.title }}</div>
    <div class="text-center text-xl mt-5">{{ articleData.description }}</div>
    <div class="text-center text-xl mt-5">{{ articleData.content }}</div>
  </div>
</template>
