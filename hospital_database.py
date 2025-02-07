import heapq
import time
from datetime import datetime

class Patient:
    def __init__(self, patient_id, name, age, severity, arrival_time, doctor_id):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.severity = severity
        self.arrival_time = arrival_time
        self.doctor_id = doctor_id

    def get_priority(self):
        severity_order = {"mild": 3, "moderate": 2, "severe": 1, "critical": 0}
        return (severity_order[self.severity], self.arrival_time)

class PatientQueue:
    def __init__(self):
        self.patient_queue = []
        self.patient_map = {}
        self.completed_consultations = []
        self.patient_id_counter = 1
        self.doctors = ["Dr. Naresh", "Dr. Chakra"]
        self.doctor_availability = {doctor: True for doctor in self.doctors}

    def add_patient(self, name, age, severity):
        try:
            if not name.replace(" ", "").isalpha():
                raise ValueError("Name must contain only alphabetic characters.")
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Age must be a positive integer.")
            if severity not in ["mild", "moderate", "severe", "critical"]:
                raise ValueError("Severity must be one of: mild, moderate, severe, critical.")

            arrival_time = time.time()
            assigned_doctor = self.get_available_doctor()
            if assigned_doctor is None:
                print("No doctors available. Please try again later.")
                return

            new_patient = Patient(self.patient_id_counter, name, age, severity, arrival_time, assigned_doctor)
            heapq.heappush(self.patient_queue, (new_patient.get_priority(), new_patient))
            self.patient_map[self.patient_id_counter] = new_patient
            self.patient_id_counter += 1
            print(f"Added: {name} (Severity: {severity}) assigned to {assigned_doctor} at {datetime.fromtimestamp(arrival_time)}")

        except ValueError as e:
            print(f"Error: {e}")

    def get_available_doctor(self):
        for doctor in self.doctors:
            if self.doctor_availability[doctor]:
                self.doctor_availability[doctor] = False
                return doctor
        return None

    def consult_patient(self):
        if not self.patient_queue:
            print("No patients are in the queue.")
            return

        _, next_patient = heapq.heappop(self.patient_queue)
        del self.patient_map[next_patient.patient_id]
        self.completed_consultations.append(next_patient)
        print(f"Consulting {next_patient.name} (Severity: {next_patient.severity}) with {next_patient.doctor_id} at {datetime.fromtimestamp(time.time())}")
        time.sleep(self.get_treatment_time(next_patient.severity))
        print(f"Patient {next_patient.name} treated by {next_patient.doctor_id} at {datetime.fromtimestamp(time.time())}.")
        self.doctor_availability[next_patient.doctor_id] = True

    def get_treatment_time(self, severity):
        severity_treatment_time = {"mild": 1, "moderate": 2, "severe": 3, "critical": 5}
        return severity_treatment_time.get(severity, 1)

    def display_queue(self):
        print("\nCurrent Patient Queue:")
        if not self.patient_queue:
            print("The queue is currently empty.")
        else:
            for _, patient in sorted(self.patient_queue, key=lambda x: x[0]):
                print(f"{patient.name} (Severity: {patient.severity}) assigned to {patient.doctor_id} at {datetime.fromtimestamp(patient.arrival_time)}")

    def view_next_patient(self):
        if not self.patient_queue:
            print("No patients are in the queue.")
            return

        _, next_patient = self.patient_queue[0]
        print(f"Next patient: {next_patient.name} (Severity: {next_patient.severity}) assigned to {next_patient.doctor_id} at {datetime.fromtimestamp(next_patient.arrival_time)}")

    def display_completed_tasks(self):
        print("\nCompleted Consultations:")
        if not self.completed_consultations:
            print("No consultations have been completed yet.")
        else:
            for patient in self.completed_consultations:
                print(f"{patient.name} (Severity: {patient.severity}) treated by {patient.doctor_id} at {datetime.fromtimestamp(patient.arrival_time)}")

patient_queue = PatientQueue()

while True:
    print("\nOptions:")
    print("1. Add Patient")
    print("2. Consult Next Patient")
    print("3. Display Current Queue")
    print("4. View Next Patient")
    print("5. Display Completed Tasks")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        try:
            name = input("Enter patient's name: ")
            if not name.replace(" ", "").isalpha():
                raise ValueError("Name must contain only alphabetic characters.")
            age = int(input("Enter patient's age: "))
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            severity = input("Enter patient's severity (mild, moderate, severe, critical): ").lower()
            if severity not in ["mild", "moderate", "severe", "critical"]:
                raise ValueError("Invalid severity level.")
            patient_queue.add_patient(name, age, severity)
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '2':
        patient_queue.consult_patient()
    elif choice == '3':
        patient_queue.display_queue()
    elif choice == '4':
        patient_queue.view_next_patient()
    elif choice == '5':
        patient_queue.display_completed_tasks()
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")