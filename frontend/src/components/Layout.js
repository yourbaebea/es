import React, { Component } from "react";

export default class Layout extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { page } = this.props; // extract the "page" prop

    return (
      <div>
        <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="/">Pharmacy</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
                        <li class="nav-item"><a class="nav-link" href="/scanner">Scanner</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        </div>
        {page}
      </div>
    );
  }
}
