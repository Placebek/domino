import axios from 'axios'

// Получаем токен из localStorage
const tokenData = JSON.parse(localStorage.getItem('user'))
const headers = { Authorization: 'Bearer ' + tokenData }

/**
 * Получить список городов
 * @param {number} skip - Количество пропущенных записей (по умолчанию 0)
 * @param {number} limit - Лимит записей (по умолчанию 10)
 * @returns {Promise<Array>} - Список городов
 */
export async function getCities(skip = 0, limit = 10) {
  try {
    const response = await axios.get(`https://py-storm.space/address/cities`, {
      headers,
      params: { skip, limit },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching cities:', error)
    return null
  }
}

/**
 * Получить список районов по ID города
 * @param {number} cityId - ID города
 * @param {number} skip - Количество пропущенных записей (по умолчанию 0)
 * @param {number} limit - Лимит записей (по умолчанию 10)
 * @returns {Promise<Array>} - Список районов
 */
export async function getDistrictsByCityId(cityId, skip = 0, limit = 10) {
  try {
    const response = await axios.get(`https://py-storm.space/address/cities/${cityId}/districts`, {
      headers,
      params: { skip, limit },
    })
    return response.data
  } catch (error) {
    console.error('Error fetching districts:', error)
    return null
  }
}

/**
 * Получить список улиц по ID района
 * @param {number} districtId - ID района
 * @param {number} skip - Количество пропущенных записей (по умолчанию 0)
 * @param {number} limit - Лимит записей (по умолчанию 10)
 * @returns {Promise<Array>} - Список улиц
 */
export async function getStreetsByDistrictId(districtId, skip = 0, limit = 10) {
  try {
    const response = await axios.get(
      `https://py-storm.space/address/districts/${districtId}/streets`,
      {
        headers,
        params: { skip, limit },
      },
    )
    return response.data
  } catch (error) {
    console.error('Error fetching streets:', error)
    return null
  }
}
