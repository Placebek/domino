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
            <option v-for="city in cities" :key="city.id" :value="city.id">
              {{ city.name }}
            </option>
          </select>
        </div>

        <!-- Район -->
        <div v-if="districts.length > 0">
          <label for="district" class="block mb-1">Районды таңдаңыз:</label>
          <select
            id="district"
            v-model="selectedDistrict"
            @change="loadStreets"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
          >
            <option value="" disabled selected>Районды таңдаңыз</option>
            <option v-for="district in districts" :key="district.id" :value="district.id">
              {{ district.name }}
            </option>
          </select>
        </div>

        <!-- Улица -->
        <div v-if="streets.length > 0">
          <label for="street" class="block mb-1">Көше таңдаңыз:</label>
          <select
            id="street"
            v-model="selectedStreet"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
          >
            <option value="" disabled selected>Көше таңдаңыз</option>
            <option v-for="street in streets" :key="street.id" :value="street.id">
              {{ street.name }}
            </option>
          </select>
        </div>

        <!-- Улица и дом -->
        <div v-if="showStreetFields">
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
            type="number"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
            placeholder="Пәтер нөмірін енгізіңіз"
          />

          <label for="floor" class="block mt-3 mb-1">Қабат:</label>
          <input
            id="floor"
            v-model="floor"
            type="number"
            class="w-[50vw] p-2 border rounded flex justify-center items-center"
            placeholder="Қабатты енгізіңіз"
          />
        </div>
      </div>
    </div>

    <div class="mb-2 bg-blue-100 p-3 rounded-md">
      <div class="font-semibold mb-2">Үйдің суреттерін жүктеу:</div>
      <input
        id="photos"
        type="file"
        multiple
        accept="image/*"
        @change="handlePhotoUpload"
        class="hidden"
        ref="fileInput"
      />
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
      <label for="name" class="block mb-1">Үйдің атауы:</label>
      <input
        id="name"
        v-model="name"
        type="text"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Үйдің атауын енгізіңіз"
      />

      <label for="description" class="block mt-3 mb-1">Сипаттама:</label>
      <textarea
        id="description"
        v-model="description"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Үйдің сипаттамасын енгізіңіз"
      ></textarea>

      <label for="price" class="block mt-3 mb-1">Үйдің бағасы (теңге):</label>
      <input
        id="price"
        v-model="price"
        type="number"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
        placeholder="Үйдің бағасын енгізіңіз"
      />

      <label for="area" class="block mt-3 mb-1">Үйдің ауданы (м²):</label>
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
        <option :value="true">Иә</option>
        <option :value="false">Жоқ</option>
      </select>

      <label for="housingType" class="block mt-3 mb-1">Тұрғын үй түрі:</label>
      <select
        id="housingType"
        v-model="housingType"
        class="w-[50vw] p-2 border rounded flex justify-center items-center"
      >
        <option value="" disabled selected>Таңдаңыз</option>
        <option value="1">Үй</option>
        <option value="2">Пәтер</option>
      </select>
    </div>

    <button
      @click="submitForm"
      class="bg-blue-500 text-white px-5 py-2 rounded hover:bg-blue-600 mb-[7vh]"
    >
      Жіберу
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getCities, getDistrictsByCityId, getStreetsByDistrictId } from '../../services/address'

const selectedCity = ref('')
const districts = ref([])
const streets = ref([])
const cities = ref([])
const selectedDistrict = ref('')
const showStreetFields = ref(false)
const street = ref('')
const houseNumber = ref('')
const apartmentNumber = ref('')
const floor = ref('')
const name = ref('')
const description = ref('')
const price = ref('')
const area = ref('')
const yearBuilt = ref('')
const rooms = ref('')
const furnished = ref('')
const housingType = ref('')
const photos = ref([])
const fileInput = ref(null)

onMounted(async () => {
  try {
    const citiesData = await getCities() // Загружаем города
    cities.value = citiesData
  } catch (error) {
    console.error('Ошибка при загрузке городов:', error)
  }
})

const loadDistricts = async () => {
  if (!selectedCity.value) {
    districts.value = []
    return
  }

  try {
    const districtsData = await getDistrictsByCityId(selectedCity.value) // Загружаем районы
    districts.value = districtsData
  } catch (error) {
    console.error('Ошибка при загрузке районов:', error)
  }

  selectedDistrict.value = '' // Сбрасываем выбранный район
  streets.value = [] // Очищаем список улиц
  showStreetFields.value = false // Скрываем поля для улиц
}

// Загрузка улиц при выборе района
const loadStreets = async () => {
  if (!selectedDistrict.value) {
    streets.value = []
    return
  }

  try {
    const streetsData = await getStreetsByDistrictId(selectedDistrict.value) // Загружаем улицы
    streets.value = streetsData
    showStreetFields.value = true // Показываем поля для улиц
  } catch (error) {
    console.error('Ошибка при загрузке улиц:', error)
  }
}

const triggerFileInput = () => {
  fileInput.value.click()
}

const handlePhotoUpload = (event) => {
  const files = Array.from(event.target.files)
  files.forEach((file) => {
    const reader = new FileReader()
    reader.onload = (e) => {
      photos.value.push({
        file,
        preview: e.target.result,
      })
    }
    reader.readAsDataURL(file)
  })
}

const removePhoto = (index) => {
  photos.value.splice(index, 1)
}

const submitForm = async () => {
  const formData = new FormData()

  formData.append('name', name.value)
  formData.append('price', parseInt(price.value, 10))
  formData.append('description', description.value)
  formData.append('house_number', houseNumber.value)
  formData.append(
    'apartment_number',
    apartmentNumber.value ? parseInt(apartmentNumber.value, 10) : null,
  )
  formData.append('floor', floor.value ? parseInt(floor.value, 10) : null)
  formData.append('type_id', parseInt(housingType.value, 10))
  formData.append('city_id', parseInt(selectedCity.value, 10))
  formData.append('district_id', parseInt(selectedDistrict.value, 10))
  formData.append('street_id', 1) // Здесь нужно заменить на реальный ID улицы, если есть
  formData.append('count_room', parseInt(rooms.value, 10))
  formData.append('is_furnished', furnished.value)
  formData.append('year_of_construction', parseInt(yearBuilt.value, 10))
  formData.append('area', parseFloat(area.value))

  // Добавляем фотографии в formData
  photos.value.forEach((photo) => {
    formData.append('photos', photo.file)
  })

  const tokenData = JSON.parse(localStorage.getItem('user'))

  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/house/create-house`, {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + tokenData,
        // 'Content-Type' не нужно указывать, потому что FormData сам установит нужный заголовок
      },
      body: formData,
    })

    if (response.ok) {
      alert('Данные успешно отправлены!')
    } else {
      alert('Ошибка при отправке данных')
    }
  } catch (error) {
    console.error('Ошибка:', error)
    alert('Произошла ошибка при отправке данных')
  }
}
</script>
