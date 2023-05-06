import React, { Component } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button
} from 'reactstrap';

export default class Login extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div className="login">
          <div className="login-form">
          <div className="mb-5">
            <h1>Login</h1>
          </div>
          <Form>
            <FormGroup>
              <Label for="email">Email address</Label>
              <Input type="email" name="email" id="email" placeholder="Enter email" />
            </FormGroup>
            <FormGroup>
              <Label for="password">Password</Label>
              <Input type="password" name="password" id="password" placeholder="Password" />
            </FormGroup>
            <Button type="submit" color="primary" className="btn-block">Submit</Button>
          </Form>

          </div>
        </div>
    );
  };
  
}
