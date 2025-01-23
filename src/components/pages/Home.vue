<script setup>
import Card from '../../components/UI/Card.vue'
import { ref, computed, onMounted } from 'vue'
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
    photos: {
      id: 1,
      url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
    },
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
    photos: {
      id: 1,
      url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
    },
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
    photos: {
      id: 1,
      url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
    },
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
    photos: {
      id: 1,
      url: 'https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510__340.jpg',
    },
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
  <div class="mt-[5vh]">
    <div class="text-3xl font-bold text-center">Дома</div>
    <div v-for="item in product" :key="item.id">
      <Card :articledata="item" />
    </div>
  </div>
</template>
