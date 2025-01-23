<script setup>
import { Form, Field } from 'vee-validate'
import * as Yup from 'yup'

import { useAuthStore } from '../../stores/auth.store.js'

const schema = Yup.object().shape({
  tg_id: Yup.string().required('tg_id is required'),
  password: Yup.string().required('Password is required'),
})

function onSubmit(values, { setErrors }) {
  const authStore = useAuthStore()
  const { tg_id, password } = values

  return authStore.login(tg_id, password).catch((error) => setErrors({ apiError: error }))
}
</script>

<template>
  <div class="relative h-screen flex justify-center items-center">
    <div class="bg-green-200 shadow-xl w-[20vw] absolute h-[40vh] rounded-2xl">
      <h2 class="flex justify-center text-[1.5vw] font-semibold mt-[3vh]">Login</h2>
      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
        <div class="flex flex-col items-center mt-[2vh]">
          <label class="text-[1vw]">tg_id</label>
          <Field
            name="tg_id"
            type="text"
            class="w-[10vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.tg_id }"
          />
          <div class="invalid-feedback">{{ errors.tg_id }}</div>
        </div>
        <div class="flex flex-col items-center mt-[2vh]">
          <label class="text-[1vw]">Password</label>
          <Field
            name="password"
            type="password"
            class="w-[10vw] rounded-lg focus:outline-none p-1 pl-2 text-[1.3vh] hover:bg-gray-100 shadow-lg"
            :class="{ 'is-invalid': errors.password }"
          />
          <div class="invalid-feedback">{{ errors.password }}</div>
        </div>
        <div class="flex items-center justify-center mt-[4vh]">
          <button
            class="bg-green-500 px-4 rounded-xl text-[1.2vw] hover:bg-green-400 shadow-xl disabled:bg-green-500"
            :disabled="isSubmitting"
          >
            <div v-show="isSubmitting" class="absolute -translate-x-1/2 left-1/2 mt-8">
              <div
                class="animate-spin rounded-full h-10 w-10 border-t-[3px] border-green-500"
              ></div>
            </div>
            Login
          </button>
        </div>
        <div v-if="errors.apiError" class="flex items-center justify-center mt-[1vh]">
          {{ errors.apiError }}
        </div>
      </Form>
    </div>
  </div>
</template>
