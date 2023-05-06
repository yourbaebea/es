import React, { Component } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button
} from 'reactstrap';

const urlRegex = /\/prescription\/(\d+)$/;


export default class Scanner extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      validUrl: false
    };
  }

  
  handleInputChange = (event) => {
    const input = event.target.value;
    const validUrl = this.isValidUrl(input);

    this.setState({
      input: input,
      validUrl: validUrl
    });
  }

  handleSubmit = (event) => {
    event.preventDefault();


    const match = this.state.input.match(urlRegex);

    if (match) {
      const id = match[1];
      window.open(this.state.input, '_blank');
      alert("Do something with the id here, such as navigate to the prescription page");
      
    } else {
      alert("Invalid URL format!");
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
    return (
        <div>
          <h1>Scan QRCode</h1>
          
          <Form onSubmit={this.handleSubmit}>
          <Input type="text" value={this.state.input} onChange={this.handleInputChange} />
          <Button disabled={!this.state.validUrl}>Go</Button>
          </Form>

        </div>
    );
  };
  
}

