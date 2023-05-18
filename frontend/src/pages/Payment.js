import React, { Component, useState } from "react";
import { checkToken } from "../utils/auth";
import axios from 'axios';
import { fetchPayment } from "../utils/api";
import CSRFToken from "../utils/CSRFToken"
import {
  Form,
  FormGroup,
  Label,
  Input,

  Button,
} from 'reactstrap';
import Cookies from 'js-cookie';

export default class Payment extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      validUrl: false,
      //token: checkToken(props)
    };

    

  }

  handleImageUpload = async (event) => {
    event.preventDefault();
    try{

    /*
    const file = event.target.files[0];
    this.setSelectedImage(URL.createObjectURL(file));
      const response = await fetchPayment(file, this.state.token);
      console.log(response.data); // Handle the response from the server
      */
    } catch (error) {
      console.error(error);
    }
  };

  setSelectedImage = (selectedImage) => {
    this.setState({ selectedImage });
  };

  render() {
    return (
      <div>
        

        <Form onSubmit={this.handleImageUpload}> 
            <FormGroup>
              <Input type="file" accept="image/*"  />
              {this.state.selectedImage && <img src={this.state.selectedImage} alt="Selected" />}
            </FormGroup>
            <Button type="submit" color="primary" className="btn-block">Submit</Button>
        </Form>





      </div>
    );
  }
}
