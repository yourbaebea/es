import React, { Component } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,

  Button
} from 'reactstrap';
import { fetchLogin } from '../components/api';
import CSRFToken from '../components/CSRFToken';
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();


export default class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      error: "",
    };
  }

  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  handleLogin = async (event) => {
    event.preventDefault();
    const { username, password } = this.state;
    console.log("user: "+ username + " password: "+ password);
    try {
      const response = await fetchLogin(username, password);
      
      console.log(response);
      //response.data.token
      this.props.setToken(response.data.token);
      //history.push('/');
      //window.location.replace('/');
    } catch (error) {
      this.setState({ error: error.message });
    }
  };

  render() {
    return (
      <div className="login">
        <div className="login-form">
          <div className="mb-5">
            <h1>Login</h1>
          </div>
          {this.state.error && (
            <div className="alert alert-danger">{this.state.error}</div>
          )}
          <Form onSubmit={this.handleLogin}> 
            <CSRFToken/>
            <FormGroup>
              <Label for="username">Username</Label>
              <Input type="text" name="username" id="username" placeholder="Enter username" onChange={this.handleInputChange}/>
            </FormGroup>
            <FormGroup>
              <Label for="password">Password</Label>
              <Input type="password" name="password" id="password" placeholder="Password" onChange={this.handleInputChange}/>
            </FormGroup>
            <Button type="submit" color="primary" className="btn-block">Submit</Button>
          </Form>
        </div>
      </div>
    );
  }
  
}
