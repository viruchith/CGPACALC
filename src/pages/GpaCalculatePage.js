import React from "react";
import { useRef,useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";
import { departments_data } from "../data";

function GpaCalculatePage() {
  const { deptid, semid } = useParams();
  const [totalCreditsDisp, setTotalCreditsDisp] = useState(0);
  const department = departments_data.find((dept) => dept.id === deptid);
  const [GPA,setGPA] = useState(undefined);
  const gpaForm = useRef();

  const calculateCredits = async()=>{
    const semData = department["sem" + semid];
    if(semData){
    let totalCredits = 0;
    semData.subjects.map((subject)=>totalCredits+=subject.credits);
    setTotalCreditsDisp(totalCredits);
    }
    
  };

  useEffect(() => {
    calculateCredits();
  })

  const gradeToPoints = (grade) => {
    if (grade === "O") {
      return 10;
    } else if (grade === "A+") {
      return 9;
    } else if (grade === "A") {
      return 8;
    } else if (grade === "B+") {
      return 7;
    } else if (grade === "B") {
      return 6;
    } else {
      return 0;
    }
  };

  if (department) {
    const semData = department["sem" + semid];
    if (semData) {
      const submitHandler = (e) => {
        e.preventDefault();
        let totalCredits = 0,
          userCredits = 0;
        let flag = false;
        const formData = new FormData(gpaForm.current);
        semData.subjects.forEach((sub) => {
          if (formData.has(sub.code)) {
            userCredits += sub.credits * gradeToPoints(formData.get(sub.code));
            totalCredits += sub.credits;
          } else {
            alert("Invalid Data !!!");
            flag = true;
            return;
          }
        });

        if (flag === false) {
          setGPA((userCredits / totalCredits).toFixed(4));
        }
      };
      return (
        <div className="main-container">
          <div className="d-flex justify-content-center">
            <div id="form-container">
              <form
                action=""
                className="container"
                method="post"
                onSubmit={submitHandler}
                ref={gpaForm}
              >
                <h2>
                  <strong>
                    {department.name} - Semester - {semid}
                  </strong>
                </h2>
                <br />
                <ol>
                  {semData.subjects.map((sub) => {
                    return (
                      <li id="form-inner-container" key={sub.code}>
                        <div className="mb-3 col-sm-6 col-md-6 animate__animated animate__wobble">
                          <label className="mb-3" htmlFor="">
                            <p>{sub.name} (<strong>{sub.code}</strong>) [ Credits : <strong>{sub.credits}</strong> ]</p>
                          </label>
                          <select
                            className="form-select"
                            name={sub.code}
                            id=""
                            required={true}
                          >
                            <option value="O" defaultChecked>
                              O
                            </option>
                            <option value="A+">A+</option>
                            <option value="A">A</option>
                            <option value="B+">B+</option>
                            <option value="B">B</option>
                            <option value="U">U</option>
                          </select>
                        </div>
                      </li>
                    );
                  })}
                </ol>
                <div className="d-flex justify-content-center">
                <div className="badge bg-dark text-light">Total Credits : {totalCreditsDisp}</div>
                </div>
                {GPA && (
                  <div className="d-flex mt-3 justify-content-center">
                    <h3>GPA : <strong>{GPA}</strong></h3>
                  </div>
                )}
                <br />
                <div className="d-flex justify-content-center">
                  <button
                    className="btn btn-warning shadow p-2 border border-dark"
                    type="submit"
                  >
                    Calculate <i className="bi-calculator-fill"></i>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      );
    } else {
      return (
        <div id="main-container">
          <h2 className="not-found p-2 text-danger">
            {department.name} Semester "{semid}" data Not Found !!!!
          </h2>
        </div>
      );
    }
  } else {
    return (
      <div id="main-container">
        <h2 className="not-found p-2 text-danger">
          Department "{deptid}" Not Found !!!!
        </h2>
      </div>
    );
  }
}

export default GpaCalculatePage;
