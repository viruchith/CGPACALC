import React from 'react'
import { Link } from 'react-router-dom'
import { departments_data } from '../data'

function NavBar() {
    const departments = departments_data;
    return (
      <nav className="navbar fixed-top navbar-expand-lg navbar-light bg-almond border border-warning">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            GPA Calc 2019 <i className="bi-book-half"></i>{" "}
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav">
              <Link className="nav-link active" aria-current="page" to="/">
                Home <i className="bi-house-door"></i>{" "}
              </Link>
              <div className="nav-item dropdown">
                {// eslint-disable-next-line
                <a
                  className="nav-link active dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Departments <i className="bi-card-list"></i>
                </a>}
                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                  {departments.map((dept) => {
                    return (
                      <li key={dept.id}>
                        {" "}
                        <Link className="dropdown-item" to={"/" + dept.id}>
                          <p>{dept.name}</p>
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              </div>
              <Link className="nav-link active" to="/about">
                About
              </Link>
            </div>
          </div>
        </div>
      </nav>
    );
}

export default NavBar
