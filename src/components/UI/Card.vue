<script>
import { Point } from './svg/svg'

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
      if (this.currentPhotoIndex > 0) {
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
          :style="{ backgroundImage: `url(${articleData.photos[currentPhotoIndex].url})` }"
        ></div>

        <!-- Основное изображение -->
        <img
          v-if="articleData.photos && articleData.photos.length > 0"
          :src="articleData.photos[currentPhotoIndex].url"
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
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 150" class="w-[25vw] h-[10vh]">
            <!-- Domino pieces -->
            <rect id="domino1" x="30" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
              <animateTransform
                attributeName="transform"
                type="rotate"
                begin="0s"
                dur="4s"
                keyTimes="0; 0.5; 1"
                values="0 40 60; 90 40 60; 90 40 60"
                fill="freeze"
                repeatCount="indefinite"
              />
            </rect>
            <rect id="domino2" x="60" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
              <animateTransform
                attributeName="transform"
                type="rotate"
                begin="0s"
                dur="4s"
                keyTimes="0; 0.125; 0.525; 1"
                values="0 70 60;0 70 60; 90 70 60; 90 70 60"
                from="0 70 60"
                to="90 70 60"
                fill="freeze"
                repeatCount="indefinite"
              />
            </rect>
            <rect id="domino3" x="90" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
              <animateTransform
                attributeName="transform"
                type="rotate"
                begin="0s"
                dur="4s"
                keyTimes="0; 0.25; 0.65; 1"
                values="0 100 60;0 100 60; 90 100 60; 90 100 60"
                from="0 100 60"
                to="90 100 60"
                fill="freeze"
                repeatCount="indefinite"
              />
            </rect>
            <rect id="domino4" x="120" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
              <animateTransform
                attributeName="transform"
                type="rotate"
                begin="0s"
                dur="4s"
                keyTimes="0; 0.375; 0.775; 1"
                values="0 130 60;0 130 60; 90 130 60; 90 130 60"
                from="0 130 60"
                to="90 130 60"
                fill="freeze"
                repeatCount="indefinite"
              />
            </rect>
            <rect id="domino5" x="150" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
              <animateTransform
                attributeName="transform"
                type="rotate"
                begin="0s"
                dur="4s"
                keyTimes="0; 0.5; 0.9; 1"
                values="0 160 60; 0 160 60; 90 160 60; 90 160 60"
                from="0 160 60"
                to="90 160 60"
                fill="freeze"
                repeatCount="indefinite"
              />
            </rect>
          </svg>
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
