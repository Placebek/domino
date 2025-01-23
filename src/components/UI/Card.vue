<script>
import { Point } from './svg/svg'
export default {
  components: {
    Point,
  },
  props: ['articledata'],
  data() {
    return {
      articleData: this.articledata,
    }
  },
  methods: {
    goToDetails() {
      this.$router.push(`/${this.articleData.id}`) // Переход на страницу с ID
    },
  },
}
</script>

<script setup>
const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}
</script>

<template>
  <div class="flex justify-center items-center mt-[2vh] cursor-pointer" @click="goToDetails">
    <div class="bg-white w-[90vw] h-[27vh] rounded-2xl shadow-lg border-2">
      <div class="w-[90vw] h-[15vh] relative flex justify-center items-center border-b-[2px]">
        <!-- Фон с размытием -->
        <div
          class="absolute inset-0 bg-cover bg-center blur-sm rounded-t-2xl"
          :style="{ backgroundImage: `url(${articleData.photos.url})` }"
        ></div>

        <!-- Основное изображение -->
        <img :src="articleData.photos.url" alt="" class="relative z-10 object-contain h-[15vh]" />
      </div>

      <div>
        <div class="text-[2.5vh] mt-2 font-semibold ml-2">
          {{ formatPrice(articleData.price) }} Тг
        </div>
      </div>

      <div class="flex gap-2 flex-row ml-2 text-[1.7vh] font-medium">
        <div class="">{{ articleData.house_type.name }}</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.character.area }} m^2</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.address.floor }}-қабат</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.character.year_of_construction }} ж</div>
      </div>

      <div>
        <div class="ml-2 text-[1.7vh] mt-[1vh]">
          {{ articleData.address.city.name }} қ., {{ articleData.address.district.name }} ауданы,
          {{ articleData.address.street.name }} көш., {{ articleData.address.house_number }}-үй
        </div>
      </div>
    </div>
  </div>
</template>
