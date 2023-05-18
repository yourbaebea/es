import React, { Component, useEffect, useState } from "react";
import { fetchPrescription } from "../utils/api";
import { checkToken } from "../utils/auth";

export default function PrescriptionDetails(props) {
  const [prescription, setPrescription] = useState(null);
  const {id} = props;
  console.log(id);

  useEffect(() => {
    let token= checkToken(props);
    async function loadPrescription() {
      try {
        const data = await fetchPrescription(id,token);
        console.log(data);
        setPrescription(data);
      } catch (error) {
        console.log(error);
        //window.location.replace('/login');
      }
    }
    loadPrescription();
  }, [id]);

  if (!prescription) {
    return <div>Loading...</div>;
  }

  return (
    <div>
    <h1>Prescription id: {prescription.prescription_id}</h1>
    <p>Expiration: {prescription.expiration}</p>
    <p>Patient: {prescription.patient}</p>
    <p>Medications:</p>
    {prescription.medications.length > 0 ?
      <ul>
        {prescription.medications.map(medication => (
          <li key={medication.medication_id}>
            {medication.name}
            {medication.alternatives.length > 0 && <div>
              <div>alternatives</div>
              <ul>
                {medication.alternatives.map(alternative => (
                  <li key={alternative.medication_id}>{alternative.name}</li>
                ))}
              </ul>
            </div>
              
            }
          </li>
        ))}
      </ul>
      : <p>No medications found.</p>
    }

    <p>Status: {prescription.status === 0 ? 'Unstarted' : prescription.status === 1 ? 'Started' : prescription.status === 2 ? 'First step' : prescription.status === 3 ? 'Second step' : prescription.status === 4 ? 'Third step' : prescription.status === 5 ? 'Finished' : 'Error'}</p>
    <p>Filled: {prescription.filled ? 'Yes' : 'No'}</p>

  </div>
  
  );
}
