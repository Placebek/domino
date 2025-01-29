<script>
import { Point } from './svg/svg'
import FallDominoAnimate from '../UI/svg/FallDominoAnimate.vue'
import DominoHomeSVG from './svg/DominoHomeSVG.vue'

export default {
  name: 'CardComponent',
  components: {
    Point,
  },
  props: ['articledata'],
  data() {
    return {
      articleData: this.articledata,
      currentPhotoIndex: 0, // Индекс текущей фотографии
      isImageLoaded: false, // Флаг для отслеживания загрузки изображения
    }
  },
  methods: {
    goToDetails() {
      this.$router.push(`/${this.articleData.id}`) // Переход на страницу с ID
    },
    nextPhoto() {
      if (this.currentPhotoIndex < this.articleData.photos.length - 1) {
        this.isImageLoaded = false // Сбрасываем флаг при смене изображения
        this.currentPhotoIndex++
      }
    },
    prevPhoto() {
      if (this.currentPhotoIndexDat0) {
        this.isImageLoaded = false // Сбрасываем флаг при смене изображения
        this.currentPhotoIndex--
      }
    },
    handleImageLoad() {
      this.isImageLoaded = true // Устанавливаем флаг после загрузки изображения
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
          v-if="articleData.photos && articleData.photos.length > 0"
          class="absolute inset-0 bg-cover bg-center blur-sm rounded-t-2xl"
          :style="{
            backgroundImage: `url(http://192.168.34.31:8000/${articleData.photos[currentPhotoIndex].photo_link})`,
          }"
        ></div>

        <!-- Основное изображение -->
        <img
          v-if="articleData.photos && articleData.photos.length > 0"
          :src="'http://192.168.34.31:8000/' + articleData.photos[currentPhotoIndex].photo_link"
          alt=""
          class="relative z-10 object-contain h-[15vh] transition-opacity duration-300"
          :class="{ 'opacity-100': isImageLoaded, 'opacity-0': !isImageLoaded }"
          loading="lazy"
          @load="handleImageLoad"
        />

        <!-- Заглушка для загрузки -->
        <div
          v-if="!isImageLoaded"
          class="absolute bg-gray-100 h-[15vh] w-[90vw] flex justify-center items-center rounded-t-2xl"
        >
          <FallDominoAnimate customClass="w-[11vw] h-[5vh]" />
        </div>
        <!-- Кнопки для переключения изображений -->
        <button
          @click.stop="prevPhoto"
          class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-60 rounded-full"
          :disabled="articleData.photos.length <= 1"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1"
            stroke="currentColor"
            class="size-7"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m11.25 9-3 3m0 0 3 3m-3-3h7.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
            />
          </svg>
        </button>
        <button
          @click.stop="nextPhoto"
          class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-60 rounded-full"
          :disabled="articleData.photos.length <= 1"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1"
            stroke="currentColor"
            class="size-7"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m12.75 15 3-3m0 0-3-3m3 3h-7.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
            />
          </svg>
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
        <div class="">{{ articleData.type.name }}</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.characteristic.area }} m^2</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.address.floor }}-қабат</div>
        <Point custom_style="mt-[0.8vh]" />
        <div class="">{{ articleData.characteristic.year_of_construction }} ж</div>
      </div>

      <div>
        <!-- <div class="ml-2 text-[1.7vh] mt-[1vh]">
          {{ articleData.address.city.name }} қ., {{ articleData.address.district.name }} ауданы,
          {{ articleData.address.street.name }} көш., {{ articleData.address.house_number }}-үй
        </div> -->
      </div>
    </div>
  </div>
</template>
