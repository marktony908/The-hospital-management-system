# cli.py

from database import Session, engine, Base
from models import Doctor, Patient, Admission

def add_doctor():
    session = Session()
    name = input("Enter the doctor's name: ")
    specialty = input("Enter the doctor's specialty: ")  # Specialty input
    new_doctor = Doctor(name=name, specialty=specialty)
    session.add(new_doctor)
    session.commit()
    print(f"Doctor {new_doctor.name} with specialty {new_doctor.specialty} added with ID {new_doctor.id}.")
    session.close()

def add_patient():
    session = Session()
    name = input("Enter the patient's name: ")
    phone_number = input("Enter the patient's phone number: ")  # Phone number input
    disease = input("Enter the patient's disease: ")  # Disease input
    new_patient = Patient(name=name, phone_number=phone_number, disease=disease)
    session.add(new_patient)
    session.commit()
    print(f"Patient {new_patient.name} with disease {new_patient.disease} added with ID {new_patient.id}.")
    session.close()

def add_admission():
    session = Session()
    patient_id = int(input("Enter the patient ID: "))
    doctor_id = int(input("Enter the doctor ID: "))
    
    new_admission = Admission(patient_id=patient_id, doctor_id=doctor_id)
    session.add(new_admission)
    session.commit()
    print(f"Admission created for patient ID {patient_id} with doctor ID {doctor_id}.")
    session.close()

def view_doctors():
    session = Session()
    doctors = session.query(Doctor).all()
    print("\nDoctors:")
    for doctor in doctors:
        print(f"ID: {doctor.id}, Name: {doctor.name}, Specialty: {doctor.specialty}")
    session.close()

def view_patients():
    session = Session()
    patients = session.query(Patient).all()
    print("\nPatients:")
    for patient in patients:
        print(f"ID: {patient.id}, Name: {patient.name}, Phone: {patient.phone_number}, Disease: {patient.disease}")
    session.close()

def view_admissions():
    session = Session()
    admissions = session.query(Admission).all()
    print("\nAdmissions:")
    for admission in admissions:
        print(f"ID: {admission.id}, Patient ID: {admission.patient_id}, Doctor ID: {admission.doctor_id}")
    session.close()

def main_menu():
    while True:
        print("\nHospital Management System")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Admission")
        print("4. View Doctors")
        print("5. View Patients")
        print("6. View Admissions")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_doctor()
        elif choice == '2':
            add_patient()
        elif choice == '3':
            add_admission()
        elif choice == '4':
            view_doctors()
        elif choice == '5':
            view_patients()
        elif choice == '6':
            view_admissions()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    main_menu()
