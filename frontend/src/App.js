import React, { Component } from "react";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import PrescriptionDetails from "./pages/PrescriptionDetails";
import PrescriptionsList from "./pages/PrescriptionsList";
import Login from "./pages/Login";
import Scanner from "./pages/Scanner";
import NotFound from "./pages/NotFound";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
  useParams
} from "react-router-dom";

function ListPrescriptionWithId(props) {
  const { id} = useParams();

  return <PrescriptionDetails id={id} token={props.token}/>;
}

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      token: props.token || null
    };
  }

  setToken = (newToken) => {
    this.setState({ token: newToken });
  };


  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <Layout page={<Home/>} token={this.props.token}/>
          </Route>
          <Route path="/login">
            <Layout page={<Login setToken={this.setToken} />} token={this.props.token}/>
          </Route>
          <Route exact path="/prescription/:id">
            <Layout page={<ListPrescriptionWithId/>} token={this.props.token}/>
          </Route>
          <Route exact path="/prescriptions">
            <Layout page={<PrescriptionsList/>} token={this.props.token}/>
          </Route>
          <Route path="/scanner">
            <Layout page={<Scanner/>} token={this.props.token}/>
          </Route>
          <Route path="*">
            <Layout page={<NotFound/>}/>
          </Route>
        </Switch>
      </Router>
    );
  }
}