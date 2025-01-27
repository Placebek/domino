<template>
  <div class="p-2">
    <div class="text-xl font-bold mb-5">Үй сату үшін осы полелерді толтырыңыз</div>

    <!-- Мекен-жай -->
    <div class="mb-2 bg-blue-100 p-3 rounded-md">
      <div class="font-semibold mb-2">Үйдің мекен-жайы:</div>
      <div class="flex flex-col gap-4">
        <!-- Город -->
        <div>
          <label for="city" class="block mb-1">Қаланы таңдаңыз:</label>
          <select
            id="city"
            v-model="selectedCity"
            @change="loadDistricts"
            class="w-[50vw] p-2 border rounded"
          >
            <option value="" disabled selected>Қаланы таңдаңыз</option>
            <option value="Алматы">Алматы</option>
            <option value="Астана">Астана</option>
            <option value="Шымкент">Шымкент</option>
          </select>
        </div>

        <!-- Район -->
        <div v-if="districts.length > 0">
          <label for="district" class="block mb-1">Районды таңдаңыз:</label>
          <select
            id="district"
            v-model="selectedDistrict"
            @change="showStreetInput"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
          >
            <option value="" disabled selected>Районды таңдаңыз</option>
            <option v-for="district in districts" :key="district" :value="district">
              {{ district }}
            </option>
          </select>
        </div>

        <!-- Улица и дом -->
        <div v-if="showStreetFields">
          <label for="street" class="block mb-1">Көше:</label>
          <input
            id="street"
            v-model="street"
            type="text"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
            placeholder="Көше атауын енгізіңіз"
          />

          <label for="houseNumber" class="block mt-3 mb-1">Үй нөмірі:</label>
          <input
            id="houseNumber"
            v-model="houseNumber"
            type="text"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
            placeholder="Үй нөмірін енгізіңіз"
          />

          <label for="apartmentNumber" class="block mt-3 mb-1"
            >Пәтер нөмірі (егер бар болса):</label
          >
          <input
            id="apartmentNumber"
            v-model="apartmentNumber"
            type="text"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
            placeholder="Пәтер нөмірін енгізіңіз"
          />
        </div>
      </div>
    </div>

    <div class="mb-2 bg-blue-100 p-3 rounded-md">
      <div class="font-semibold mb-2">Үйдің суреттерін жүктеу:</div>
      <!-- Скрываем стандартный input -->
      <input
        id="photos"
        type="file"
        multiple
        accept="image/*"
        @change="handlePhotoUpload"
        class="hidden"
        ref="fileInput"
      />
      <!-- Кастомная кнопка -->
      <button
        @click="triggerFileInput"
        class="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600"
      >
        📁 Суреттерді таңдау
      </button>
      <div v-if="photos.length > 0" class="mt-3">
        <p class="mb-2">Таңдалған суреттер:</p>
        <div class="flex flex-wrap gap-4">
          <div
            v-for="(photo, index) in photos"
            :key="index"
            class="relative w-24 h-24 border rounded overflow-hidden"
          >
            <img :src="photo.preview" alt="Preview" class="object-cover w-full h-full" />
            <button
              @click="removePhoto(index)"
              class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-5 h-5 text-xs flex items-center justify-center"
            >
              ×
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Дополнительные поля -->
    <div class="mb-2 bg-blue-100 p-3 rounded-md">
      <div class="font-semibold mb-2">Қосымша ақпарат:</div>
      <label for="area" class="block mb-1">Үйдің ауданы (м²):</label>
      <input
        id="area"
        v-model="area"
        type="number"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Үйдің ауданын енгізіңіз"
      />

      <label for="yearBuilt" class="block mt-3 mb-1">Қай жылы құрылған?</label>
      <input
        id="yearBuilt"
        v-model="yearBuilt"
        type="number"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Құрылған жылын енгізіңіз"
      />

      <label for="price" class="block mt-3 mb-1">Үйдің бағасы (теңге):</label>
      <input
        id="price"
        v-model="price"
        type="number"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Үйдің бағасын енгізіңіз"
      />

      <label for="rooms" class="block mt-3 mb-1">Бөлмелер саны:</label>
      <input
        id="rooms"
        v-model="rooms"
        type="number"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Бөлмелер санын енгізіңіз"
      />

      <label for="furnished" class="block mt-3 mb-1">Үй жиһаздалған ба?</label>
      <select
        id="furnished"
        v-model="furnished"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
      >
        <option value="" disabled selected>Таңдаңыз</option>
        <option value="Иә">Иә</option>
        <option value="Жоқ">Жоқ</option>
      </select>

      <label for="heating" class="block mt-3 mb-1">Жылу түрі:</label>
      <select
        id="heating"
        v-model="heating"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
      >
        <option value="" disabled selected>Таңдаңыз</option>
        <option value="Орталықтандырылған">Орталықтандырылған</option>
        <option value="Жеке">Жеке</option>
        <option value="Газ">Газ</option>
        <option value="Электр">Электр</option>
      </select>

      <label for="housingType" class="block mt-3 mb-1">Тұрғын үй түрі:</label>
      <select
        id="housingType"
        v-model="housingType"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
      >
        <option value="" disabled selected>Таңдаңыз</option>
        <option value="Үй">Үй</option>
        <option value="Пәтер">Пәтер</option>
      </select>
    </div>

    <!-- Контактные данные -->
    <div class="mb-2 bg-blue-100 p-3 rounded-md">
      <div class="font-semibold mb-2">Байланыс деректері:</div>
      <label for="contactName" class="block mb-1">Аты-жөні:</label>
      <input
        id="contactName"
        v-model="contactName"
        type="text"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Атыңызды енгізіңіз"
      />

      <label for="contactPhone" class="block mt-3 mb-1">Телефон нөмірі:</label>
      <input
        id="contactPhone"
        v-model="contactPhone"
        type="tel"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Телефон нөмірін енгізіңіз"
      />
    </div>

    <button class="bg-blue-500 text-white px-5 py-2 rounded hover:bg-blue-600 mb-[7vh]">
      Жіберу
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedCity = ref('')
const districts = ref([])
const selectedDistrict = ref('')
const showStreetFields = ref(false)
const street = ref('')
const houseNumber = ref('')
const apartmentNumber = ref('')
const area = ref('')
const yearBuilt = ref('')
const price = ref('')
const rooms = ref('')
const furnished = ref('')
const heating = ref('')
const housingType = ref('')
const contactName = ref('')
const contactPhone = ref('')
const photos = ref([])
const fileInput = ref(null)

const triggerFileInput = () => {
  fileInput.value.click()
}
// Обработка загруженных фотографий
const handlePhotoUpload = (event) => {
  const files = Array.from(event.target.files) // Преобразуем FileList в массив
  files.forEach((file) => {
    const reader = new FileReader()
    reader.onload = (e) => {
      photos.value.push({
        file,
        preview: e.target.result, // Превью изображения (base64)
      })
    }
    reader.readAsDataURL(file) // Преобразуем файл в base64
  })
}

// Удаление фотографии
const removePhoto = (index) => {
  photos.value.splice(index, 1)
}
// Загружаем районы в зависимости от города
const loadDistricts = () => {
  if (selectedCity.value === 'Алматы') {
    districts.value = ['Алатау', 'Бостандық', 'Медеу', 'Наурызбай']
  } else if (selectedCity.value === 'Астана') {
    districts.value = ['Байқоңыр', 'Есіл', 'Сарыарқа', 'Алматы']
  } else if (selectedCity.value === 'Шымкент') {
    districts.value = ['Абай', 'Әл-Фараби', 'Еңбекші', 'Қаратау']
  } else {
    districts.value = []
  }
  selectedDistrict.value = ''
  showStreetFields.value = false
}

// Показываем поля для улицы и дома
const showStreetInput = () => {
  showStreetFields.value = !!selectedDistrict.value
}
</script>

<style scoped>
/* Дополнительные стили для удобства */
</style>
