import React, { Component, setState } from "react";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import PrescriptionDetails from "./pages/PrescriptionDetails";
import PrescriptionsList from "./pages/PrescriptionsList";
import Login from "./pages/Login";
import Scanner from "./pages/Scanner";
import NotFound from "./pages/NotFound";
import history from "./utils/history"

import {
  BrowserRouter,
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
      <BrowserRouter history={history}>
        <Switch>
          <Route exact path="/">
            <Layout page={<Home />}/>
          </Route>
          <Route path="/login" render={(props) => (
            <Layout page={<Login {...props} />}/>
          )} />
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
      </BrowserRouter>
    );
  }
}
