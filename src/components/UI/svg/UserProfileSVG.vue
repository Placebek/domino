<template>
  <svg
    :class="customClass"
    :fill="fillColor"
    :width="width"
    :height="height"
    :stroke-width="strokeWidthCustom"
    :stroke="strokeColorCustom"
    version="1.1"
    id="Layer_1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    viewBox="0 0 24 24"
    xml:space="preserve"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
    />
  </svg>
</template>

<script>
export default {
  name: 'UserProfileSVG',
  props: {
    customClass: {
      type: String,
      default: '',
    },
    fillColor: {
      type: String,
      default: 'none',
    },
    width: {
      type: String,
      default: '100px',
    },
    strokeWidthCustom: {
      type: String,
      default: '1.2',
    },
    strokeColorCustom: {
      type: String,
      default: '#000000',
    },
    height: {
      type: String,
      default: '100px',
    },
  },
}
</script>
