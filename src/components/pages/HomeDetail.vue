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
          :style="{ backgroundImage: `url(${house.photos[currentPhotoIndex].photo_link})` }"
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
              :src="photo.photo_link"
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
              {{ house.address.city.id }} қ., {{ house.address.city.district.name }} ауданы,
              {{ house.address.city.district.street.name }} көш.,
              {{ house.address.house_number }}-үй
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
              <div>{{ house.characteristic.area }} м^2</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Бөлме саны:</div>
              <div>{{ house.characteristic.count_room }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Қабат:</div>
              <div>{{ house.address.floor }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Жиһазы:</div>
              <div>{{ house.characteristic.is_furnished ? 'Бар' : 'Жоқ' }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Құралған жылы:</div>
              <div>{{ house.characteristic.year_of_construction }} жыл</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Үй типі:</div>
              <div>{{ house.type.name }}</div>
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
              <div>{{ house.address.city }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Район:</div>
              <div>{{ house.address.district }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Көшесі:</div>
              <div>{{ house.address.street }}</div>
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
              <div>{{ house.seller[0].user.firstname }} {{ house.seller[0].user.lastname }}</div>
            </div>
            <div class="flex flex-row">
              <div class="w-[40vw] text-gray-500">Телефон:</div>
              <div>{{ house.seller[0].user.phone_number }}</div>
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
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

export default {
  name: 'HomeDetail',
  setup() {
    const house = ref(null)
    const currentPhotoIndex = ref(0)
    const touchStartX = ref(0)
    const touchEndX = ref(0)
    const route = useRoute()

    const fetchHouse = async () => {
      const houseId = route.params.id
      try {
        const response = await axios.get(
          `${import.meta.env.VITE_API_URL}/house/get-house/${houseId}`,
        )
        house.value = response.data
      } catch (error) {
        console.error('Ошибка при загрузке данных:', error)
      }
    }

    const prevPhoto = () => {
      if (currentPhotoIndex.value > 0) {
        currentPhotoIndex.value--
      }
    }

    const nextPhoto = () => {
      if (currentPhotoIndex.value < house.value.photos.length - 1) {
        currentPhotoIndex.value++
      }
    }

    const onTouchStart = (event) => {
      touchStartX.value = event.changedTouches[0].screenX
    }

    const onTouchEnd = (event) => {
      touchEndX.value = event.changedTouches[0].screenX
      handleSwipe()
    }

    const handleSwipe = () => {
      const swipeDistance = touchEndX.value - touchStartX.value
      if (swipeDistance > 50) {
        prevPhoto()
      } else if (swipeDistance < -50) {
        nextPhoto()
      }
    }

    const formatPrice = (price) => {
      return new Intl.NumberFormat('ru-RU').format(price)
    }

    onMounted(() => {
      fetchHouse()
    })

    return {
      house,
      currentPhotoIndex,
      prevPhoto,
      nextPhoto,
      onTouchStart,
      onTouchEnd,
      formatPrice,
    }
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
