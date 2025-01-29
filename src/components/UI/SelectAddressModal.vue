<template>
  <div v-if="isModalOpen" class="fixed inset-0 bg-black/50 flex items-center justify-center">
    <div class="bg-white rounded-[15px] shadow-2xl w-[80vw] h-[50vh] p-5 mx-auto mt-[10vh]">
      <div class="flex flex-col">
        <!-- Поле поиска -->
        <input
          type="text"
          placeholder="Search city..."
          v-model="search"
          class="border-[1px] rounded-[10px] h-[4vh] shadow-inner px-[2.5vw] focus:outline-lime-500 mb-[2vh]"
        />
        <!-- Список городов -->
        <div class="overflow-y-auto max-h-[30vh] border-[1px] p-[1vh] border-lime-500">
          <div
            v-for="city in filteredCities"
            :key="city.id"
            class="py-2 px-4 hover:bg-lime-200 cursor-pointer rounded-md border-[1px]"
            @click="handleCitySelect(city.city_name)"
          >
            {{ city.city_name }}
          </div>
        </div>
        <!-- Кнопка закрытия -->
        <button
          class="py-2 px-4 bg-red-500 text-white rounded-md self-end mt-[2vh]"
          @click="closeModal"
        >
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isModalOpen: {
      type: Boolean,
      required: true,
    },
    cities: {
      type: Array,
      required: true,
    },
    search: {
      type: String,
      required: true,
    },
  },
  emits: ['update:isModalOpen', 'update:search', 'city-select'],
  computed: {
    filteredCities() {
      return this.cities.filter((city) =>
        city.city_name.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  methods: {
    closeModal() {
      this.$emit('update:isModalOpen', false);
    },
    handleCitySelect(cityName) {
      this.$emit('city-select', cityName);
      this.closeModal();
    },
  },
};
</script>

<style scoped>
/* Стили можно добавить сюда при необходимости */
</style>
