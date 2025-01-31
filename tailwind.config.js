module.exports = {
  content: ['./src/**/*.{vue,js,jsx}'],
  theme: {
    extend: {
      backgroundImage: {
        'domino-login': "url('/src/assets/img/domino_bg_login_lite.jpg')", // Замените путь на свой
      },
      boxShadow: {
        'custom-inset': '0px 5px 10px 2px rgba(34, 60, 80, 0.2) inset',
      }
    },
  },
  // plugins: [require('tailwindcss-primeui')],
}
