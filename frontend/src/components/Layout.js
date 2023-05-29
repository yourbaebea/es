import React, { Component } from "react";
import instance from '../utils/axios';

export default class Layout extends Component {
  constructor(props) {
    super(props);
  }

  removeCookie = async (event) => {
    event.preventDefault();
    document.cookie = 'BearerToken=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;';

    instance.defaults.headers.common['Authorization'] = null;

    window.location.replace('/');
  };

  render() {
    const { page } = this.props; // extract the "page" prop

    return (
      <div>
        <div>
          <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container">
              <a className="navbar-brand" href="/">
                Pharmacy
              </a>
              <div>
                <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                  <li className="nav-item">
                    <a className="nav-link" href="/">
                      Home
                    </a>
                  </li>
                  <li className="nav-item">
                    <a className="nav-link" href="/scanner">
                      Scanner
                    </a>
                  </li>
                  <li className="nav-item">
                    <a className="nav-link" href="/login">
                      Login
                    </a>
                  </li>
                  <li className="nav-item">
                    <a className="nav-link" onClick={this.removeCookie}>
                      Logout
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </nav>
        </div>
        <div style={{ padding: '20px 20px' }}>{page}</div>
      </div>
    );
  }
}
