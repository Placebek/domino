<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import { Form, Field } from 'vee-validate'
import * as Yup from 'yup'

import { useAuthStore } from '../../stores/auth.store.js'

const schema = Yup.object().shape({
  phone_number: Yup.string().required('Телефон номеріңізді жазу керек'),
  password: Yup.string().required('Құпия сөзді жазу керек'),
})

async function onSubmit(values, { setErrors }) {
  const authStore = useAuthStore()
  const { phone_number, password } = values

  try {
    await authStore.login(phone_number.toString(), password)
  } catch (error) {
    setErrors({ apiError: error })
  }
}
</script>

<template>
  <div class="relative h-screen flex justify-center items-center bg-domino-login">
    <div class="bg-blue-300/95 shadow-xl w-[60vw] absolute max-h-[40vh] rounded-2xl pb-[2vh]">
      <h2 class="flex justify-center text-[3vh] font-semibold mt-[3vh]">Кіру</h2>
      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
        <div class="flex flex-col items-center mt-[2vh]">
          <Field
            placeholder="Телефон номеріңіз"
            name="phone_number"
            type="number"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.phone_number }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.phone_number }}</div>
        </div>
        <div class="flex flex-col items-center mt-[1.3vh]">
          <Field
            placeholder="Құпия сөз"
            name="password"
            type="password"
            class="w-[40vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.password }"
          />
          <div class="invalid-feedback leading-4 text-[1.3vh]">{{ errors.password }}</div>
        </div>
        <div class="flex items-center justify-center mt-[2vh]">
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
        <div>
          <router-link
            to="/register"
            class="flex items-center justify-center mt-[1vh] font-semibold text-blue-500"
          >
            Жаңа аккаунт жасау
          </router-link>
        </div>
      </Form>
    </div>
  </div>
</template>
