import React from 'react'
import { Link } from 'react-router-dom';
import { departments_data } from '../data';

function IndexPage() {
    const departments = departments_data;
    return (
      <>
      <div id="main-container">
        <ul id="dept-list">
          {departments.map((dept) => {
            return (
              <li className="dept-list-item animate__animated animate__tada" key={dept.id}>
                <Link to={"/" + dept.id}>
                  <img
                    className="img"
                    src={"/images/" + dept.id + ".png"}
                    alt={dept.name}
                  />
                </Link>
                <br />
                <p>
                  <Link to={"/"+dept.id}>{dept.name}</Link>
                </p>
              </li>
            );
          })}
        </ul>
      </div>
      </>
    );
}

export default IndexPage
