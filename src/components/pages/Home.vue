<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import Card from '../../components/UI/Card.vue'
import logo from '../../assets/img/logo_domino.png'
import { ref, onMounted } from 'vue'
import { getHouses } from '../../services/houses'
const product = ref([])

const isLoading = ref(true)

onMounted(async () => {
  isLoading.value = true
  const response = await getHouses()
  if (response) {
    product.value = response.data
    isLoading.value = false
  } else {
    isLoading.value = false
  }
})

// const filteredProducts = computed(() => {
//   return Array.isArray(product.value)
//     ? product.value.filter((post) => post.request_id === null)
//     : []
// })
</script>

<template>
  <div class="flex flex-col">
    <div
      class="relative w-[30vw] h-[12vh] lg:w-[19vw] lg:h-[29vh] md:w-[15vw] md:h-[25vh] xl:w-[25vw] xl:h-[35vh] 2xl:w-[30vw] 2xl:h-[40vh]"
    >
      <img :src="logo" alt="" />
    </div>
    <div
      class="ml-[2vw] bg-blue-200 px-[3vw] py-[1vh] mt-[2vh] w-[96vw] mr-[2vw] rounded-md relative"
    >
      <div>
        Фильтрлер:
        <div class="flex flex-row">
          <div class="w-[40vw]">
            Қаланы таңдаңыз:
            <select class="w-[30vw]">
              <option>Алматы</option>
              <option>Астана</option>
              <option>Алматы</option>
              <option>Алматы</option>
            </select>
          </div>
          <div>
            <div>Район:</div>

            <select class="w-[30vw]">
              <option>Алатау</option>
              <option>Алатау</option>
              <option>Алатау</option>
              <option>Алатау</option>
            </select>
          </div>
        </div>
        <div class="flex flex-row gap-x-[5vw]">
          <div>
            <div>Улица:</div>
            <select class="w-[30vw]">
              <option>Абая</option>
              <option>Абая</option>
              <option>Абая</option>
              <option>Абая</option>
            </select>
          </div>
          <button
            class="bg-blue-500 text-white rounded-lg h-[4vh] px-[3vw] mt-[2vh] absolute right-[5vw] bottom-[1vh]"
          >
            Іздеу
          </button>
          <div
            class="text-blue-500 cursor-pointer mt-[2vh] absolute top-0 right-2 underline font-bold flex flex-row"
          >
            <div>Көбірек</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-5"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.75 12h16.5m-16.5 3.75h16.5M3.75 19.5h16.5M5.625 4.5h12.75a1.875 1.875 0 0 1 0 3.75H5.625a1.875 1.875 0 0 1 0-3.75Z"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="text-3xl font-bold text-center">Дома</div>
    <div>
      <div v-if="product.length === 0">
        <div v-if="isLoading" class="flex justify-center items-center mt-[5vh]">
          <div
            class="animate-spin rounded-full h-10 w-10 border-t-2 border-b-2 border-blue-500"
          ></div>
        </div>
        <div v-else class="text-center text-[3vh] font-semibold mt-[2vh]">Ештеңе жоқ</div>
      </div>
      <div v-else>
        <div v-for="item in product" :key="item.id">
          <Card :articledata="item" />
        </div>
      </div>
    </div>
  </div>
</template>
