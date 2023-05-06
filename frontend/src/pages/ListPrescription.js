import React, { Component, useEffect, useState } from "react";

export default function ListPrescription(props) {
  const [prescription, setPrescription] = useState(null);
  const id = props.id;
  console.log(id);

  useEffect(() => {
    async function fetchPrescription() {
      const response = await fetch(`/api/prescription/${id}`);
      const data = await response.json();
      setPrescription(data);
    }
    fetchPrescription();
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
            {medication.alternatives.length > 0 &&
              <ul>
                {medication.alternatives.map(alternative => (
                  <li key={alternative.medication_id}>{alternative.name}</li>
                ))}
              </ul>
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
