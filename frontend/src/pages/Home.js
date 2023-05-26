import React, { Component } from "react";
import { checkToken } from "../utils/auth";

export default class Home extends Component {
  constructor(props) {
    super(props);

    checkToken(props);
  }

  render() {
    return (
        <div>
            <h1>Home</h1>
            <p>This Pharmacy works!</p>
        </div>
    
    );
  }
}
