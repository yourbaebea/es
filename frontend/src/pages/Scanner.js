import React, { Component } from "react";
import { checkToken } from "../utils/auth";
import { Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { fetchPrescriptionData, fetchStartOrder } from "../utils/api";
import CSRFToken from '../utils/CSRFToken'
import axios from 'axios';

const urlRegex = /\/prescription\/(\d+)$/;

export default class Scanner extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      validUrl: false,
      prescription: null,
      total:null,
    };

    checkToken(props);
  }

  handleInputChange = (event) => {
    const input = event.target.value;
    const validUrl = this.isValidUrl(input);

    this.setState({
      input,
      validUrl,
    });
  }

  updatePrescription(prescription){
    let total=0;
    prescription.medications.forEach((medication) => {
      total=total+ medication.price;
    });

    this.setState({ prescription: prescription, total: total });
  }


  async fetchPrescriptions(id) {
    try {
      const response = await fetchPrescriptionData(id);

      const prescription = response.data.prescription[0];
      
      this.updatePrescription(prescription);

    } catch (error) {
      console.error("Error fetching prescriptions:", error);
    }
  }




  handleSubmit = async (event) => {
    event.preventDefault();

    console.log(this.state.input)
    
    const match = this.state.input.match(urlRegex);

    console.log(match);

    if (match!=null) {
      const id = match[1];
      this.fetchPrescriptions(id);
        
      
    } else {
      alert("Invalid URL format!");
    }
  }

  handleStart = async (event) => {
    event.preventDefault();

    const response = await fetchStartOrder(this.state.prescription);
    console.log("res");
    console.log(response);
    console.log(response.data);
    console.log(response.data.order_status);

    if(response.data.update!=null){

    window.alert(`Starting Step Functions success, created order in dynamicdb.\n\njust for debug ${response.data.order_status}`);
    window.location.replace(`/payment/${this.state.prescription.prescription_id}`);
    }
    else{
      window.alert(`error creating order in dynamicdb: ${response.data.order_status}`);
    }
    
  }

  handleReplacement = async (med, alt) => {
    // Make the necessary changes to replace the medication with the selected alternative
    // Reload the prescription after making the changes
    const { prescription } = this.state;


  // Find the medication in the prescription and remove all alternatives
    prescription.medications.forEach((medication) => {
      if (medication.medication_id === med.medication_id) {
        medication.alternatives = [];
        // Add the selected alternative to the medication
        medication.medication_id = alt.medication_id;
        medication.name = alt.name;
        medication.price = alt.price;
      }
    });
    this.updatePrescription(prescription);
  }

  isValidUrl = (url) => {
    try {
      new URL(url);
      return true;
    } catch (_) {
      return false;
    }
  }

  render() {
    const { input, validUrl, prescription, total } = this.state;

    return (
      <div>
        {prescription ? (
          <div>
            <h1>Confirm Prescription</h1>
            <h3>Prescription id: {prescription.prescription_id}</h3>
            <p>Expiration: {prescription.expiration}</p>
            <p>Patient: {prescription.patient}</p>
            <p>Medications:</p>
            {prescription.medications.length > 0 ? (
              <ul>
                {prescription.medications.map(medication => (
                  <li key={medication.medication_id}>
                    {medication.name}: {medication.price} €
                    {medication.alternatives.length > 0 ? (
                      <div>
                        <div>Options</div>
                        <ul>
                          {medication.alternatives.map(alternative => (
                            <div>
                              <li key={alternative.medication_id}>
                                
                                <Button
                                  onClick={() => this.handleReplacement(medication, alternative)}
                                  color="primary"
                                  className="btn-block">
                                  {alternative.name}: {alternative.price} €
                                </Button>
                              </li>
                            </div>
                            
                            



                          ))}
                        </ul>
                      </div>
                    ):(<div>
                        <div>No other options</div>
                      </div>)}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No medications found.</p>
            )}
            <p>Status: {prescription.status === 0 ? 'Unstarted' : prescription.status === 1 ? 'Started' : prescription.status === 2 ? 'First step' : prescription.status === 3 ? 'Second step' : prescription.status === 4 ? 'Third step' : prescription.status === 5 ? 'Finished' : 'Error'}</p>
            <p>Filled: {prescription.filled ? 'Yes' : 'No'}</p>
          

            <h3>Price: {total} €</h3>

            <Form onSubmit={this.handleStart}>
              <Button color="success">Go to Payment</Button>
            </Form>
          </div>
        ) : (
          <div>

            <h1>Scan QRCode</h1>
            <Form onSubmit={this.handleSubmit}>
              <CSRFToken/>
              <Input type="text" value={input} onChange={this.handleInputChange} />
              <Button color="success" disabled={!validUrl}>Get Prescription</Button>
            </Form>

            <div> Waiting to Read Qr Code...</div>
            

          </div>
        )}

        


        
      </div>
    );
  }
}
