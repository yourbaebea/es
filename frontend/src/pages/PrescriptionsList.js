import React, { Component, useEffect, useState } from "react";
import { checkToken } from "../utils/auth";

export default function PrescriptionsList(props) {
  const [prescriptions, setPrescription] = useState(null);

  

  useEffect(() => {
    checkToken(props);
    async function fetchPrescription() {
      const response = await fetch(`/api/prescriptions/`);
      const data = await response.json();
      setPrescription(data);
    }
    fetchPrescription();
  });

  if (!prescriptions) {
    return <div>Loading...</div>;
  }

  return (
      <div>
        <h1>Prescriptions</h1>
        {prescriptions.length > 0 ? (
          <table class="table">
          <thead>
            <tr>
              <th scope="col">Prescription ID</th>
              <th scope="col">Expiration</th>
              <th scope="col">Patient</th>
              <th scope="col">Status</th>
              <th scope="col">Filled</th>
            </tr>
          </thead>
            <tbody>
              {prescriptions.map((prescription) => (
                <tr key={prescription.prescription_id}>
                  <td scope="row">{prescription.prescription_id}</td>
                  <td>{prescription.expiration}</td>
                  <td>{prescription.patient}</td>
                  <td>
                    {prescription.status === 0
                      ? "Unstarted"
                      : prescription.status === 1
                      ? "Started"
                      : prescription.status === 2
                      ? "First step"
                      : prescription.status === 3
                      ? "Second step"
                      : prescription.status === 4
                      ? "Third step"
                      : prescription.status === 5
                      ? "Finished"
                      : "Error"}
                  </td>
                  <td>{prescription.filled ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No prescriptions found.</p>
        )}
        </div>
      
      
    );
}
