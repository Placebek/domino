<template>
  <div class="bg-white rounded-xl shadow-md relative">
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
      <!-- Слайдер -->
      <div
        class="slider-container w-full h-[40vh] relative overflow-hidden"
        @touchstart="onTouchStart"
        @touchend="onTouchEnd"
      >
        <!-- Лента изображений -->
        <div
          class="slider-track flex transition-transform duration-500"
          :style="{ transform: `translateX(-${currentPhotoIndex * 100}%)` }"
        >
          <!-- Каждое изображение -->
          <div
            v-for="(photo, index) in house.photos"
            :key="index"
            class="slider-item min-w-full flex-shrink-0"
          >
            <img :src="photo.url" alt="" class="w-full h-full object-cover" loading="lazy" />
          </div>
        </div>
      </div>
      <!-- Кнопки переключения -->
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
export default {
  name: 'HomeDetail',
  data() {
    return {
      house: null,
      currentPhotoIndex: 0,
      touchStartX: 0,
      touchEndX: 0,
    }
  },
  async created() {
    const id = Number(this.$route.params.id)

    // Моковые данные
    const mockHouses = [
      {
        id: 1,
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
.slider-container {
  position: relative;
  overflow: hidden;
  border-bottom: 2px solid #ccc;
  border-radius: 8px;
}

.slider-track {
  display: flex;
  transition: transform 0.5s ease;
}

.slider-item {
  min-width: 100%;
  flex-shrink: 0;
  overflow: hidden;
}
</style>
