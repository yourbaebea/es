import React, { Component } from "react";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import ListPrescription from "./pages/ListPrescription";
import Login from "./pages/Login";
import Scanner from "./pages/Scanner";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
  useParams
} from "react-router-dom";

function ListPrescriptionWithId() {
  const { id } = useParams();

  return <ListPrescription id={id} />;
}

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <Layout page={<Home/>}/>
          </Route>
          <Route path="/login">
            <Layout page={<Login/>}/>
          </Route>
          <Route exact path="/prescription/:id">
            <Layout page={<ListPrescriptionWithId/>}/>
          </Route>
          <Route path="/scanner">
            <Layout page={<Scanner/>}/>
          </Route>
        </Switch>
      </Router>
    );
  }
}