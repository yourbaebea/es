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

function ListPrescriptionWithId() {
  const { id} = useParams();

  return <PrescriptionDetails id={id}/>;
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
          <Route exact path="/prescriptions">
            <Layout page={<PrescriptionsList/>}/>
          </Route>
          <Route path="/scanner">
            <Layout page={<Scanner/>}/>
          </Route>
          <Route path="*">
            <Layout page={<NotFound/>}/>
          </Route>
        </Switch>
      </Router>
    );
  }
}