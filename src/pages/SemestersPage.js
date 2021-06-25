import React from 'react'
import { useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { departments_data } from '../data';

function SemestersPage() {
    const semesters = [...Array(8).keys()];
    const {deptid} = useParams();
    const department = departments_data.find((dept)=>dept.id===deptid);
    useEffect(()=>{
      window.scrollTo(0,0);
    },[department])
    if(department){
return (
  <div id="main-container">
    <div className="d-flex justify-content-center p-5">
      <img
        className="img p-1 bg-almond border border-warning rounded"
        src={"/images/" + department.id + ".png"}
        alt={department.name}
      />
    </div>
    <div className="d-flex justify-content-center">
      <div className="badge bg-warning text-dark p-2">
        <p>
          <strong>{department.name}</strong>
        </p>
      </div>
    </div>
    <ul id="sem-list">
      {semesters.map((sem) => {
        return department["sem" + (sem + 1)] ? (
          <li key={"sem" + (sem + 1)}>
            <Link to={"/" + deptid + "/sem/" + (sem + 1)}>
              <div className="sem-list-item animate__animated animate__rubberBand">
                <Link to={"/" + deptid + "/sem/" + (sem + 1)}>
                  {" "}
                  <strong>Semester - {sem + 1}</strong>{" "}
                </Link>
              </div>
            </Link>
          </li>
        ) : (
          <li key={"sem" + (sem + 1)}>
            <div className="sem-list-item">
              <strong>Semester - {sem + 1}</strong>
              <br />
              <small>
                <strong>unavailable</strong>
              </small>
            </div>
          </li>
        );
      })}
    </ul>
  </div>
);
    }else{
        return <div id="main-container">
            <h2 className="not-found p-2 text-danger">Department "{deptid}" Not Found !!!!</h2>
        </div>
    }
    
}

export default SemestersPage
