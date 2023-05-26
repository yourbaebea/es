import React, { Component, useState } from "react";
import { checkToken } from "../utils/auth";
import axios from 'axios';
import { fetchPayment, fetchUpdateOrder, fetchFacialRekognition } from "../utils/api";
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
      selectedImage: null,
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
    const imgFile = this.state.selectedImage; // Get the selected file

    try{

      const response = await fetchFacialRekognition(imgFile);

      if(response.data.rekognition!=null){
        window.alert(`Facial Rekognition: ${response.data.rekognition}, payment is already completed and another lambda function is updating order status on dynamicdb`);

        //window.location.replace(`/status/${this.state.prescription.prescription_id}`);
        window.location.replace("/");
   

      }
      else{
        window.alert(`Facial Rekognition Error: ${response.data.error}`);
        this.setState({selectedImage : null });
      }
      


    } catch (error) {
      console.error(error);
    }
  };


  setSelectedImage = async (event) => {
    const selectedImage = event.target.files[0];

    this.setState({selectedImage : selectedImage });
  };

  render() {
    return (
      <div>
        

        <Form onSubmit={this.handleImageUpload} enctype="multipart/form-data"> 
            <FormGroup>
              <Input type="file" accept="image/*" name="image" onChange={this.setSelectedImage} />
              {this.state.selectedImage && (<img src={URL.createObjectURL(this.state.selectedImage)} alt="Selected" style={{ width: '200px', height: '200px' }} />)}
    </FormGroup>
            
            <Button type="submit" color="primary" className="btn-block">Submit Image</Button>
            
        
        </Form>

      </div>
    );
  }
}
