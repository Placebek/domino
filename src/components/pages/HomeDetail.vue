<template>
  <div class="bg-white rounded-xl shadow-md space-y-4 relative">
    <!-- Кнопка назад -->
    <button
      @click="$router.push('/')"
      class="absolute top-4 left-4 px-[2vw] py-[1vh] bg-white text-white rounded-lg z-20"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="3"
        stroke="black"
        class="size-6"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18"
        />
      </svg>
    </button>

    <div v-if="house">
      <div>
        <div
          class="w-full h-[40vh] relative flex justify-center items-center border-b-[2px] overflow-hidden"
          @touchstart="onTouchStart"
          @touchend="onTouchEnd"
        >
          <!-- Фон с эффектом blur -->
          <div
            v-if="house.photos && house.photos.length > 0"
            class="absolute inset-0 bg-cover bg-center blur-sm rounded-t-2xl"
            :style="{ backgroundImage: `url(${house.photos[currentPhotoIndex].url})` }"
          ></div>

          <!-- Анимация -->
          <FallDominoAnimate customClass="w-[30vw] h-[10vh]" />

          <!-- Основное изображение -->
          <img
            v-if="house.photos && house.photos.length > 0"
            :src="house.photos[currentPhotoIndex].url"
            alt=""
            class="relative z-10 object-contain h-[40vh] transition-opacity duration-300"
            :class="{ 'opacity-100': isImageLoaded, 'opacity-0': !isImageLoaded }"
            loading="lazy"
            @load="handleImageLoad"
          />
        </div>
        <div class="flex justify-between mt-2">
          <button
            @click="prevPhoto"
            :disabled="currentPhotoIndex === 0"
            class="px-4 py-2 bg-blue-500 text-white rounded-lg"
          >
            Prev
          </button>
          <button
            @click="nextPhoto"
            :disabled="currentPhotoIndex === house.photos.length - 1"
            class="px-4 py-2 bg-blue-500 text-white rounded-lg"
          >
            Next
          </button>
        </div>
      </div>
      <div class="mt-4">
        <p class="text-gray-900 font-bold"><strong>Price:</strong> ${{ house.price }}</p>
        <p class="text-gray-700"><strong>Description:</strong> {{ house.description }}</p>
      </div>
    </div>
    <div v-else>
      <p class="flex justify-center items-center h-[70vh] text-[4vh] font-serif font-semibold">
        Үй табылмады
      </p>
    </div>
  </div>
</template>

<script>
import FallDominoAnimate from '../UI/svg/FallDominoAnimate.vue'

export default {
  name: 'HomeDetail',
  data() {
    return {
      house: null, // Данные о доме
      currentPhotoIndex: 0, // Индекс текущего фото
      touchStartX: 0, // Начальная точка касания
      touchEndX: 0, // Конечная точка касания
    }
  },
  components: {
    FallDominoAnimate,
  },
  async created() {
    const id = Number(this.$route.params.id)

    // Моковые данные
    const mockHouses = [
      {
        id: 1,
        address: {
          id: 1,
          city: { id: 1, name: 'Алматы' },
          district: { id: 1, name: 'Алатау' },
          street: { id: 1, name: 'Абая' },
          house_number: 1,
          apartment_number: 1,
          floor: 1,
        },
        house_type: { id: 1, name: 'Вторичка' },
        photos: [
          {
            id: 1,
            url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
          },
          {
            id: 2,
            url: 'https://images.unsplash.com/photo-1737405555489-78b3755eaa81?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
          },
          {
            id: 3,
            url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
          },
        ],
        price: 10000000,
        description: 'Описание дома',
        character: {
          id: 1,
          count_rooms: 3,
          is_with_furniture: true,
          year_of_construction: 2020,
          area: 100,
        },
        is_sold: false,
      },
    ]

    this.house = mockHouses.find((house) => house.id === id) || null
  },
  methods: {
    prevPhoto() {
      if (this.currentPhotoIndex > 0) {
        this.currentPhotoIndex--
      }
    },
    nextPhoto() {
      if (this.currentPhotoIndex < this.house.photos.length - 1) {
        this.currentPhotoIndex++
      }
    },
    handleImageLoad() {
      this.isImageLoaded = true
    },
    onTouchStart(event) {
      this.touchStartX = event.changedTouches[0].screenX
    },
    onTouchEnd(event) {
      this.touchEndX = event.changedTouches[0].screenX
      this.handleSwipe()
    },
    handleSwipe() {
      const swipeDistance = this.touchEndX - this.touchStartX
      if (swipeDistance > 50) {
        this.prevPhoto()
      } else if (swipeDistance < -50) {
        this.nextPhoto()
      }
    },
  },
}
</script>

<style>
/* Дополнительные стили */
</style>
