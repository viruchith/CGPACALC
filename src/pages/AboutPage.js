import React from 'react'
import { Link } from 'react-router-dom';

function AboutPage() {
    return (
      <div className="main-container">
        <div className="d-flex justify-content-center">
          <div className="inner-container p-4">
            <h3>
              <strong>About : </strong>
            </h3>
            <br />
            <p>
              A GPA caclculator built specially for Sona College of Technology
              2019 Regulation syllabus.
            </p>
            <code>Source code - </code>
            <Link to={{pathname:"https://github.com/viruchith/CGPACALC"}} target="_blank">
              <i className="bi-github"></i>.
            </Link>
            <br/><br/>
            <h5>
              Special Credits to <strong>Shrishtidharan K.A.</strong>
            </h5>
            <br />
            <h3>
              <strong>Contact</strong>
            </h3>
            <br />
            <h5>
              <strong>Email : </strong>
              <a href="mailto:contact@viruchith.com">contact@viruchith.com</a>
            </h5>
          </div>
        </div>
      </div>
    );
}

export default AboutPage
