import axios from 'axios'
const tokenData = JSON.parse(localStorage.getItem('user'))?.access_token
const headers = { Authorization: 'Bearer ' + tokenData }

export async function getHouses() {
  try {
    const response = await axios(
      'http://192.168.69.31:8000/house/get-houses',
      { headers },
      // { referrerPolicy: 'unsafe-url' },
    )
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error fetching data:', error)
    return null
  }
}

export async function getHousesByID(id) {
  try {
    const response = await axios(
      `http://192.168.69.31:8000/auth/admin/requests/${id}`,
      { headers },
      { referrerPolicy: 'unsafe-url' },
    )
    return response.data
  } catch (error) {
    console.error('Error fetching data:', error)
    return null
  }
}
