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
  <div class="flex justify-center items-center">
    <div class="bg-white w-[90vw] h-[20vh] rounded-lg shadow-lg">
      <div class="w-full h-[10vh]">
        <img :src="articleData.photos.url" alt="" />
      </div>
      <div class="text-center text-lg mt-2">{{ articleData.price }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.house_type.name }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.character.area }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.character.count_rooms }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.character.year_of_construction }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.character.is_with_furniture }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.city.name }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.district.name }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.street.name }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.house_number }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.apartment_number }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.address.floor }}</div>
      <div class="text-center text-lg mt-2">{{ articleData.description }}</div>
    </div>
  </div>
</template>
