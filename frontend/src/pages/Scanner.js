import React, { Component } from "react";
import { checkToken } from "../utils/auth";
import { Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { fetchPrescription } from "../utils/api";

const urlRegex = /\/prescription\/(\d+)$/;

export default class Scanner extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      validUrl: false,
      prescription: null,
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

  handleSubmit = async (event) => {
    event.preventDefault();

    console.log(this.state.input)

    const match = this.state.input.match(urlRegex);

    console.log(match);

    if (match!=null) {
      const id = match[1];

      async function fetchPrescription() {
        const response = await fetch(`/api/prescription/${id}`);
        const data = await response.json();
        console.log(data)
        this.setState({
          prescription: data,
        });
      }
      fetchPrescription();
        
      
    } else {
      alert("Invalid URL format!");
    }
  }

  handleReplacement = async (alternativeId) => {
    // Make the necessary changes to replace the medication with the selected alternative
    // Reload the prescription after making the changes
    const { prescription } = this.state;

    try {
      // Perform the replacement logic
      // ...

      // Reload the prescription
      const data = await fetchPrescription(prescription.id, checkToken(this.props));
      this.setState({
        prescription: data,
      });
    } catch (error) {
      console.log(error);
      window.location.replace('/login');
    }
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
    const { input, validUrl, prescription } = this.state;

    return (
      <div>
        <h1>Scan QRCode</h1>
        <Form onSubmit={this.handleSubmit}>
          <Input type="text" value={input} onChange={this.handleInputChange} />
          <Button disabled={!validUrl}>Go</Button>
        </Form>

        {prescription ? (
          <div>
            <h1>Prescription id: {prescription.prescription_id}</h1>
            <p>Expiration: {prescription.expiration}</p>
            <p>Patient: {prescription.patient}</p>
            <p>Medications:</p>
            {prescription.medications.length > 0 ? (
              <ul>
                {prescription.medications.map(medication => (
                  <li key={medication.medication_id}>
                    {medication.name}
                    {medication.alternatives.length > 0 && (
                      <div>
                        <div>Alternatives</div>
                        <ul>
                          {medication.alternatives.map(alternative => (
                            <li key={alternative.medication_id}>
                              {alternative.name}
                              <Button
                                onClick={() => this.handleReplacement(alternative.medication_id)}
                                color="primary"
                                className="btn-block"
                              >
                                Select this
                              </Button>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No medications found.</p>
            )}
            <p>Status: {prescription.status === 0 ? 'Unstarted' : prescription.status === 1 ? 'Started' : prescription.status === 2 ? 'First step' : prescription.status === 3 ? 'Second step' : prescription.status === 4 ? 'Third step' : prescription.status === 5 ? 'Finished' : 'Error'}</p>
            <p>Filled: {prescription.filled ? 'Yes' : 'No'}</p>
          </div>
        ) : (
          <div>Waiting to Read Qr Code...</div>
        )}
      </div>
    );
  }
}
