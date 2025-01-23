<script setup>
import { Form, Field } from 'vee-validate'
import * as Yup from 'yup'

import { useAuthStore } from '../../stores/auth.store.js'

const schema = Yup.object().shape({
  phone_number: Yup.string().required('Телефон номеріңізді жазу керек'),
  password: Yup.string().required('Құпия сөзді жазу керек'),
})

function onSubmit(values, { setErrors }) {
  const authStore = useAuthStore()
  const { phone_number, password } = values

  return authStore.login(phone_number, password).catch((error) => setErrors({ apiError: error }))
}
</script>

<template>
  <div class="relative h-screen flex justify-center items-center bg-domino-login">
    <div class="bg-blue-300/95 shadow-xl w-[60vw] absolute h-[40vh] rounded-2xl">
      <h2 class="flex justify-center text-[3vh] font-semibold mt-[3vh]">Кіру</h2>
      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
        <div class="flex flex-col items-center mt-[2vh]">
          <label class="text-[2vh]">Телефон номеріңіз</label>
          <Field
            name="phone_number"
            type="text"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.phone_number }"
          />
          <div class="invalid-feedback">{{ errors.phone_number }}</div>
        </div>
        <div class="flex flex-col items-center mt-[2vh]">
          <label class="text-[2vh]">Құпия сөз</label>
          <Field
            name="password"
            type="password"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.password }"
          />
          <div class="invalid-feedback">{{ errors.password }}</div>
        </div>
        <div class="flex items-center justify-center mt-[4vh]">
          <button
            class="bg-blue-500 px-4 rounded-xl text-[2vh] font-medium text-white hover:bg-blue-400 shadow-xl disabled:bg-blue-500"
            :disabled="isSubmitting"
          >
            <div v-show="isSubmitting" class="absolute -translate-x-1/2 left-1/2 mt-8">
              <div class="animate-spin rounded-full h-10 w-10 border-t-[3px] border-blue-500"></div>
            </div>
            Кіріп кету
          </button>
        </div>
        <div v-if="errors.apiError" class="flex items-center justify-center mt-[1vh]">
          {{ errors.apiError }}
        </div>
      </Form>
    </div>
  </div>
</template>
