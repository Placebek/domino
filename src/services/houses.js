import axios from 'axios'
const tokenData = JSON.parse(localStorage.getItem('user'))
const headers = { Authorization: 'Bearer ' + tokenData }

export async function getHouses() {
  try {
    const response = await axios(
      `https://py-storm.space/house/get-houses`,
      { headers },
      // { referrerPolicy: 'unsafe-url' },
    )
    const data = await response
    return data
  } catch (error) {
    console.error('Error fetching data:', error)
    return null
  }
}

export async function getHousesByID(id) {
  try {
    const response = await axios(
      `https://py-storm.space/house/get-houses/${id}`,
      { headers },
      { referrerPolicy: 'unsafe-url' },
    )
    return response.data
  } catch (error) {
    console.error('Error fetching data:', error)
    return null
  }
}
