<template>
  <div class="bg-white rounded-xl shadow-md relative">
    <!-- Кнопка назад -->
    <button
      @click="$router.push('/')"
      class="absolute top-2 left-2 px-[2vw] py-[1vh] bg-white text-black rounded-lg z-20 shadow-sm hover:bg-gray-100"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="3"
        stroke="currentColor"
        class="w-6 h-6"
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
        class="slider-container w-full h-[40vh] relative overflow-hidden rounded-t-2xl"
        @touchstart="onTouchStart"
        @touchend="onTouchEnd"
      >
        <!-- Размытый фон -->
        <div
          v-if="house.photos && house.photos.length > 0"
          class="absolute inset-0 bg-cover bg-center blur-lg"
          :style="{ backgroundImage: `url(${house.photos[currentPhotoIndex].url})` }"
        ></div>

        <!-- Лента изображений -->
        <div
          class="slider-track flex transition-transform duration-500 relative z-10"
          :style="{ transform: `translateX(-${currentPhotoIndex * 100}%)` }"
        >
          <div
            v-for="(photo, index) in house.photos"
            :key="index"
            class="slider-item min-w-full flex-shrink-0"
          >
            <img
              :src="photo.url"
              alt="House photo"
              class="w-[100vw] h-[40vh] object-contain"
              loading="lazy"
            />
          </div>
        </div>
        <div class="absolute top-[1vh] right-[3vw] text-[2vh] text-white font-medium">
          {{ currentPhotoIndex + 1 }} / {{ house.photos.length }}
        </div>
      </div>

      <!-- Информация о доме -->
      <div
        class="flex absolute top-[36vh] transform bg-white rounded-t-[20px] w-full items-center flex-col"
      >
        <div class="mt-4 px-4 bg-blue-100 w-[95vw] rounded-lg shadow-md">
          <p class="text-gray-900 font-bold text-[3vh]">{{ formatPrice(house.price) }} Тг</p>
          <div>
            <div class="text-[2vh] font-semibold">
              {{ house.address.city.name }} қ., {{ house.address.district.name }} ауданы,
              {{ house.address.street.name }} көш., {{ house.address.house_number }}-үй
            </div>
          </div>
        </div>
        <div>
          <div class="text-[2vh] mt-4 p-2 bg-blue-100 w-[95vw] rounded-lg shadow-md">
            <div class="font-semibold text-[2.2vh]">Қысқаша сипаттамасы:</div>
            {{ house.description }}
          </div>
        </div>
        <div
          class="flex flex-col bg-blue-100 w-[95vw] rounded-lg shadow-md mt-4 p-2 text-[2vh] font-semibold"
        >
          <div class="font-semibold text-[2.2vh]">Пәтер сипаттамасы:</div>
          <div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Ауданы:</div>
              <div>{{ house.character.area }} м^2</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Бөлме саны:</div>
              <div>{{ house.character.count_rooms }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Қабат:</div>
              <div>{{ house.address.floor }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Жиһазы:</div>
              <div>{{ house.character.is_with_furniture ? 'Бар' : 'Жоқ' }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Құралған жылы:</div>
              <div>{{ house.character.year_of_construction }} жыл</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Үй типі:</div>
              <div>{{ house.house_type.name }}</div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col bg-blue-100 w-[95vw] rounded-lg shadow-md mt-4 p-2 text-[2vh] font-semibold"
        >
          Мекен-жайы:
          <div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Қала:</div>
              <div>{{ house.address.city.name }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Район:</div>
              <div>{{ house.address.district.name }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Көшесі:</div>
              <div>{{ house.address.street.name }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Үй нөмірі:</div>
              <div>{{ house.address.house_number }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Пәтер нөмірі:</div>
              <div>{{ house.address.apartment_number }}</div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col bg-blue-100 w-[95vw] rounded-lg shadow-md mt-4 p-2 text-[2vh] font-semibold mb-[7vh]"
        >
          <div>Үй иесі туралы ақпарат:</div>
          <div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Аты:</div>
              <div>Айдос</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Телефон:</div>
              <div>+7 777 777 77 77</div>
            </div>
          </div>
          <div>
            <button
              class="bg-blue-500 text-white rounded-lg px-4 py-2 mt-2 hover:bg-blue-600"
              @click="$router.push('/video')"
            >
              Видеокамера арқылы байланысқа шығу
            </button>
          </div>
        </div>
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
        address: {
          id: 1,
          city: {
            id: 1,
            name: 'Алматы',
          },
          district: {
            id: 1,
            name: 'Алатау',
          },
          street: {
            id: 1,
            name: 'Абая',
          },
          house_number: 1,
          apartment_number: 1,
          floor: 1,
        },
        house_type: {
          id: 1,
          name: 'Вторичка',
        },
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
        description: 'Описание дома ',
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
    formatPrice(price) {
      return new Intl.NumberFormat('ru-RU').format(price)
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
