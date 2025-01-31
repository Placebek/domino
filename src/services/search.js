import axios from 'axios';

// Получаем токен из localStorage
const tokenData = JSON.parse(localStorage.getItem('user'));
const headers = { Authorization: 'Bearer ' + tokenData?.token }; // Добавляем проверку на наличие токена

// Функция для поиска домов
export async function searchHouses(query) {
  try {
    const response = await axios.get('https://py-storm.space/search/houses', {
      headers,
      params: {
        query,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при выполнении поиска:', error);
    return null;
  }
}