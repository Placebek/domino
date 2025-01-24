<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import Card from '../../components/UI/Card.vue'
import logo from '../../assets/img/logo_domino.png'
import { ref } from 'vue'
// import { getHouses } from '../../services/houses'
const product = ref([
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
      { id: 1, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
      {
        id: 2,
        url: 'https://images.unsplash.com/photo-1737405555489-78b3755eaa81?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      },
      { id: 3, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
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
  {
    id: 2,
    address: {
      id: 2,
      city: {
        id: 2,
        name: 'Астана',
      },
      district: {
        id: 2,
        name: 'Алатау',
      },
      street: {
        id: 2,
        name: 'Абая',
      },
      house_number: 2,
      apartment_number: 2,
      floor: 2,
    },
    house_type: {
      id: 2,
      name: 'Вторичка',
    },
    photos: [
      { id: 1, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
      {
        id: 2,
        url: 'https://images.unsplash.com/photo-1737405555489-78b3755eaa81?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      },
      { id: 3, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
    ],
    price: 20000000,
    description: 'Описание дома 2',
    character: {
      id: 2,
      count_rooms: 4,
      is_with_furniture: false,
      year_of_construction: 2021,
      area: 200,
    },
    is_sold: false,
  },
  {
    id: 3,
    address: {
      id: 3,
      city: {
        id: 3,
        name: 'Алматы',
      },
      district: {
        id: 3,
        name: 'Алатау',
      },
      street: {
        id: 3,
        name: 'Абая',
      },
      house_number: 3,
      apartment_number: 3,
      floor: 3,
    },
    house_type: {
      id: 3,
      name: 'Вторичка',
    },
    photos: [
      { id: 1, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
      {
        id: 2,
        url: 'https://images.unsplash.com/photo-1737405555489-78b3755eaa81?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      },
      { id: 3, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
    ],
    price: 30000000,
    description: 'Описание дома 3',
    character: {
      id: 3,
      count_rooms: 5,
      is_with_furniture: true,
      year_of_construction: 2022,
      area: 300,
    },
    is_sold: false,
  },
  {
    id: 4,
    address: {
      id: 4,
      city: {
        id: 4,
        name: 'Алматы',
      },
      district: {
        id: 4,
        name: 'Алатау',
      },
      street: {
        id: 4,
        name: 'Абая',
      },
      house_number: 4,
      apartment_number: 4,
      floor: 4,
    },
    house_type: {
      id: 4,
      name: 'Вторичка',
    },
    photos: [
      { id: 1, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
      {
        id: 2,
        url: 'https://images.unsplash.com/photo-1737405555489-78b3755eaa81?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      },
      { id: 3, url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg' },
    ],
    price: 40000000,
    description: 'Описание дома 4',
    character: {
      id: 4,
      count_rooms: 6,
      is_with_furniture: false,
      year_of_construction: 2023,
      area: 400,
    },
    is_sold: false,
  },
])
// const isLoading = ref(true)

// onMounted(async () => {
//   isLoading.value = trueғ
//   const response = await getHouses()
//   if (response) {
//     product.value = response
//     isLoading.value = false
//   } else {
//     isLoading.value = false
//   }
// })

// const filteredProducts = computed(() => {
//   return Array.isArray(product.value)
//     ? product.value.filter((post) => post.request_id === null)
//     : []
// })
</script>

<template>
  <div class="flex flex-col">
    <div class="w-[30vw] h-[10vh]">
      <img :src="logo" alt="" />
    </div>
    <div class="ml-[2vw] bg-blue-200 p-2 mt-[2vh] w-[96vw] mr-[2vw] rounded-md relative">
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
            class="bg-blue-500 text-white rounded-lg h-[4vh] px-[3vw] mt-[2vh] absolute right-[10vw]"
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
    <div v-for="item in product" :key="item.id">
      <Card :articledata="item" />
    </div>
  </div>
</template>
