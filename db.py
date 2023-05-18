'''import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta


import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'users'

# Define the user details
username = 'john_doe'
password = 'example123'
email = 'john.doe@example.com'

# Put the user item into the User table
response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'username': {'S': username},
        'password': {'S': password},
        'email': {'S': email}
    }
)

# Print the response
print("User added successfully:", response)


# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'PrescriptionsTable'  # Choose a suitable table name

class Pacient:
    def __init__(self, name, username, email, password, pharmacist=False):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.pharmacist = pharmacist

    def save(self):
        table = dynamodb.Table('Pacients')
        table.put_item(
            Item={
                'username': self.username,
                'name': self.name,
                'email': self.email,
                'password': self.password,
                'pharmacist': self.pharmacist
            }
        )

    def __str__(self):
        return f'{self.username}'

class Medication:
    def __init__(self, name, alternatives=None, price=10):
        self.name = name
        self.alternatives = alternatives or []
        self.price = price

    def save(self):
        table = dynamodb.Table('Medications')
        table.put_item(
            Item={
                'name': self.name,
                'alternatives': self.alternatives,
                'price': self.price
            }
        )

    def __str__(self):
        return f'{self.name}'

class Prescription:
    def __init__(self, patient, filled=False):
        self.patient = patient
        self.medications = []
        self.filled = filled
        self.expiration_date = datetime.now() + timedelta(days=30)
        self.status = 0  # Assuming status.UNSTARTED is mapped to 0

    def save(self):
        table = dynamodb.Table('Prescriptions')
        table.put_item(
            Item={
                'patient': self.patient.username,
                'medications': [medication.name for medication in self.medications],
                'filled': self.filled,
                'expiration_date': self.expiration_date.isoformat(),
                'status': self.status
            }
        )

    def __str__(self):
        return f'Prescription for {self.patient}, status: {self.status}'

class PrescriptionMedication:
    def __init__(self, prescription, medication, dosage):
        self.prescription = prescription
        self.medication = medication
        self.dosage = dosage

    def save(self):
        table = dynamodb.Table('PrescriptionMedications')
        table.put_item(
            Item={
                'prescription': self.prescription,
                'medication': self.medication,
                'dosage': self.dosage
            }
        )


# Create tables
def create_tables():
    try:
        # Create the Pacients table
        pacients_table = dynamodb.create_table(
            TableName='Pacients',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        pacients_table.wait_until_exists()

        # Create the Medications table
        medications_table = dynamodb.create_table(
            TableName='Medications',
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        medications_table.wait_until_exists()

        # Create the Prescriptions table
        prescriptions_table = dynamodb.create_table(
            TableName='Prescriptions',
            KeySchema=[
                {
                    'AttributeName': 'patient',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'patient',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        prescriptions_table.wait_until_exists()

        # Create the PrescriptionMedications table
        prescription_medications_table = dynamodb.create_table(
            TableName='PrescriptionMedications',
            KeySchema=[
                {
                    'AttributeName': 'prescription',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'medication',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'prescription',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'medication',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        prescription_medications_table.wait_until_exists()

        # Add items to tables
        pacient = Pacient('John Doe', 'johndoe', 'john@example.com', 'password', pharmacist=False)
        pacient.save()

        medication = Medication('Medicine A', alternatives=['Medicine B'], price=15)
        medication.save()

        patient = Pacient('Jane Smith', 'janesmith', 'jane@example.com', 'password', pharmacist=True)
        prescription = Prescription(patient, filled=False)
        prescription.medications.append(medication)
        prescription.save()

        prescription_medication = PrescriptionMedication('prescription_1', 'medication_1', 2)
        prescription_medication.save()

        print('Tables created successfully.')

    except ClientError as e:
        print(f'Error creating tables: {e}')

# Call the create_tables function
create_tables()
'''