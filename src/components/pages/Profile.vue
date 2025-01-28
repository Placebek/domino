<template>
  <div class="relative h-screen flex justify-center items-center ">
    <div class="bg-blue-300/95 shadow-xl w-[70vw] absolute max-h-[55vh] rounded-2xl pb-[2vh]">
      <h2 class="flex text-center justify-center text-[3vh] font-semibold mt-[3vh]">Профиль</h2>
      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
        <!-- Поле имени -->
        <div class="flex flex-col items-center mt-[2vh]">
          <Field
            placeholder="Атыңыз"
            name="first_name"
            type="text"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.first_name }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.first_name }}</div>
        </div>

        <!-- Поле фамилии -->
        <div class="flex flex-col items-center mt-[1.3vh]">
          <Field
            name="last_name"
            placeholder="Тегіңіз"
            type="text"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.last_name }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.last_name }}</div>
        </div>

        <!-- Поле Email -->
        <div class="flex flex-col items-center mt-[1.3vh]">
          <Field
            placeholder="Email"
            name="email"
            type="email"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.email }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.email }}</div>
        </div>

        <!-- Поле телефона -->
        <div class="flex flex-col items-center mt-[1.3vh]">
          <Field
            placeholder="Телефон номеріңіз"
            name="phone"
            type="tel"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.phone }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.phone }}</div>
        </div>

        <!-- Кнопка отправки -->
        <div class="flex justify-center mt-[2vh]">
          <button
            type="submit"
            :disabled="isSubmitting"
            class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-6 rounded-lg shadow-md disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ isSubmitting ? 'Жіберілуде...' : 'Сақтау' }}
          </button>
        </div>
      </Form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useForm, Field, Form } from 'vee-validate'
import * as yup from 'yup'

// Валидация
const schema = yup.object({
  first_name: yup.string().required('Атыңызды енгізіңіз'),
  last_name: yup.string().required('Тегіңізді енгізіңіз'),
  email: yup.string().email('Жарамды Email енгізіңіз').required('Email қажет'),
  phone: yup.string().required('Телефон номеріңізді енгізіңіз'),
})

// Модель формы
const form = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
})

// Функция загрузки данных профиля
const getProfile = async () => {
  try {
    const response = await fetch('/api/profile', { method: 'GET' })
    const data = await response.json()
    form.value = {
      first_name: data.first_name || '',
      last_name: data.last_name || '',
      email: data.email || '',
      phone: data.phone || '',
    }
  } catch (error) {
    console.error('Ошибка загрузки профиля:', error)
  }
}

// Функция отправки формы
const onSubmit = async (values) => {
  try {
    const response = await fetch('/api/profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })

    if (!response.ok) {
      throw new Error('Ошибка сохранения профиля')
    }

    alert('Профиль успешно сохранен!')
  } catch (error) {
    console.error('Ошибка сохранения:', error)
    alert('Ошибка сохранения профиля.')
  }
}

// Загружаем профиль при монтировании компонента
onMounted(() => {
  getProfile()
})
</script>

<style scoped>
/* Можно добавить дополнительные стили */
button {
  transition: all 0.3s;
}
button:hover {
  transform: scale(1.05);
}
</style>
