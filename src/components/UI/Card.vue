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
      currentPhotoIndex: 0, // Индекс текущей фотографии
    }
  },
  methods: {
    goToDetails() {
      this.$router.push(`/${this.articleData.id}`) // Переход на страницу с ID
    },
    nextPhoto() {
      if (this.currentPhotoIndex < this.articleData.photos.length - 1) {
        this.currentPhotoIndex++
      } else {
        this.currentPhotoIndex = 0 // Если достигли последней фотографии, переходим на первую
      }
    },
    prevPhoto() {
      if (this.currentPhotoIndex > 0) {
        this.currentPhotoIndex--
      } else {
        this.currentPhotoIndex = this.articleData.photos.length - 1 // Если на первой, то переходим на последнюю
      }
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
  <div class="flex justify-center items-center mt-[2vh] cursor-pointer" @click="">
    <div class="bg-white w-[90vw] h-[27vh] rounded-2xl shadow-lg border-2">
      <div class="w-[90vw] h-[15vh] relative flex justify-center items-center border-b-[2px]">
        <!-- Фон с размытием -->
        <div
          v-if="articleData.photos && articleData.photos.length > 0"
          class="absolute inset-0 bg-cover bg-center blur-sm rounded-t-2xl"
          :style="{ backgroundImage: `url(${articleData.photos[currentPhotoIndex].url})` }"
        ></div>

        <!-- Основное изображение -->
        <img
          v-if="articleData.photos && articleData.photos.length > 0"
          :src="articleData.photos[currentPhotoIndex].url"
          alt=""
          class="relative z-10 object-contain h-[15vh]"
        />

        <!-- Кнопки для переключения изображений -->
        <button
          @click="prevPhoto"
          class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-60 p-2 rounded-full"
          :disabled="articleData.photos.length <= 1"
        >
          ←
        </button>
        <button
          @click="nextPhoto"
          class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-60 p-2 rounded-full"
          :disabled="articleData.photos.length <= 1"
        >
          →
        </button>
        <div class="absolute bottom-1 left-1 text-[1.5vh] text-white font-medium">
          {{ currentPhotoIndex + 1 }} / {{ articleData.photos.length }}
        </div>
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

      <!-- Индикатор текущего положения -->
    </div>
  </div>
</template>
