import React, { Component, useState } from "react";
import { checkToken } from "../utils/auth";
import axios from 'axios';
import { fetchPayment, fetchUpdateOrder } from "../utils/api";
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
      id: null,
      input: '',
      validUrl: false,
      //token: checkToken(props)
    };

  }

  componentDidMount() {
    const { match } = this.props;
    const { id } = match.params;

    console.log('Prescription ID:', id);
    this.setState({id: id});

    // Use the prescription ID for further processing in the payment page
  }

  async updatePaymentOrder() {
    try {
      //TODO this is the function name in aws
      const update_function= "updatePaymentOrder"
      const response = await fetchUpdateOrder(this.state.id,update_function );
      console.log(response);


    } catch (error) {
      console.error("Error :", error);
    }
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

  handleConfirmation = async (event) => {
    event.preventDefault();
    
    this.updatePaymentOrder()
    
    window.alert('Facial Rekognition success, payment is done and another lambda function is updating order status on dynamicdb');

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
            <Button type="submit" color="primary" className="btn-block">Submit Image</Button>
            
        
        </Form>

        <Button onClick={this.handleConfirmation} color="secondary" className="btn-block">
          Confirm Payment
        </Button>





      </div>
    );
  }
}
