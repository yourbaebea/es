// api.js
import Cookies from 'js-cookie';
import axios from 'axios';

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
    const res = await axios.post(`/api/login`, body, config);

    console.log("response in fetch arrived:");
    console.log(res.data);

    return res;

} catch(err) {
  throw new Error("Ah shit. Here we go again. " + err);
}
};




/*
export async function fetchLogin(username, password) {
    try {
        console.log("inside handle login REACT")
        const response = await fetch(`/api/login`, {
            method: "POST",
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken')
            },
            body: JSON.stringify({username, password }),
        });
        
        console.log("inside handle login REACT before sending response, csrftoken: "+ Cookies.get('csrftoken'))
        const data = await response.json();
        console.log("inside handle login REACT after sending response")
        if (response.ok) {
            return data.token;
        } else {
            throw new Error(data.message);
        }
    } catch (error) {
        //console.error(error);
        throw new Error("Something went wrong. Please try again later.");
    }
  };
  */


export async function fetchPrescription(id,token) {
    const response = await fetch(`/api/prescription/${id}`);
  
    if (response.status === 200) {
      const data = await response.json();
      console.log(data);
      return data;
    } else if (response.status === 401) {
      throw new Error('Unauthorized');
    } else {
      throw new Error('Something went wrong');
    }
  }