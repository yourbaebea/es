// api.js
import Cookies from 'js-cookie';
import instance from '../utils/axios';

export async function fetchLogin(username, password){
  const config = {
      headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': Cookies.get('csrftoken')
      }
  };

const body = JSON.stringify({ username, password });

try {
    const res = await instance.post(`/api/login`, body, config);

    console.log("response in fetch arrived:");
    console.log(res.data);

    instance.defaults.headers.common['Authorization'] = `Bearer ${res.data.token}`;

    return res;

} catch(err) {
  throw new Error("Ah sht. Here we go again. " + err);
}
};

export async function fetchPrescriptionData(id) {
  const config = {
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
};
  try {
    const response = await instance.post('/api/order', { id }, config);
    return response;
  } catch (error) {
    throw new Error("Error fetching prescriptions:", error);
  }
}

export async function fetchStartOrder(order) {
  const config = {
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
};
  try {
    const response = await instance.post('/api/startorder', { order }, config);
    return response;
  } catch (error) {
    throw new Error("Error starting order:", error);
  }
}

export async function fetchUpdateOrder(id,update_function) {
  const config = {
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
  };
  try {
    const response = await instance.post('/api/updateorder', { id, update_function }, config);
    return response;
  } catch (error) {
    throw new Error("Error starting order:", error);
  }
}

export async function fetchFacialRekognition(img){
  const config = {
      headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': Cookies.get('csrftoken')
      }
  };

  const formData = new FormData();
  formData.append('image', img);

try {
    const res = await instance.post(`/api/rekognition`, formData, config);

    console.log("response in fetch arrived:");
    console.log(res.data);

    return res;

} catch(err) {
  throw new Error("Ah sht. Here we go again. " + err);
}
};
