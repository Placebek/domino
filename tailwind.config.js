module.exports = {
  content: ['./src/**/*.{vue,js,jsx}'],
  theme: {
    extend: {
      backgroundImage: {
        'domino-login': "url('/src/assets/img/domino_bg_login_lite.jpg')", // Замените путь на свой
      },
    },
  },
  // plugins: [require('tailwindcss-primeui')],
}
