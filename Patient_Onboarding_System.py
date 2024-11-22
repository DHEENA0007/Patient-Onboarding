class PatientOnboardingSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        print("\n--- Add Patient Details ---")
        patient_id = input("Enter Patient ID: ")
        
        # Check for duplicate IDs
        if any(patient['ID'] == patient_id for patient in self.patients):
            print("Error: Patient with this ID already exists!\n")
            return

        patient = {
            'ID': patient_id,
            'Name': input("Enter Patient Name: "),
            'Age': input("Enter Patient Age: "),
            'Gender': input("Enter Patient Gender (M/F): "),
            'Phone': input("Enter Patient Phone Number: "),
            'Address': input("Enter Patient Address: "),
            'MedicalHistory': input("Enter Patient Medical History: ")
        }
        self.patients.append(patient)
        print("Patient added successfully!\n")

    def view_patients(self):
        print("\n--- List of Patients ---")
        if not self.patients:
            print("No patients registered yet.\n")
            return
        for patient in self.patients:
            print(f"ID: {patient['ID']}, Name: {patient['Name']}, Age: {patient['Age']}, Gender: {patient['Gender']}, "
                  f"Phone: {patient['Phone']}, Address: {patient['Address']}, Medical History: {patient['MedicalHistory']}")
        print()

    def search_patient(self):
        print("\n--- Search Patient ---")
        patient_id = input("Enter Patient ID to search: ")
        for patient in self.patients:
            if patient['ID'] == patient_id:
                print(f"Patient found: {patient}")
                return
        print("Patient not found!\n")

    def update_patient(self):
        print("\n--- Update Patient Details ---")
        patient_id = input("Enter Patient ID to update: ")
        for patient in self.patients:
            if patient['ID'] == patient_id:
                print("Patient found. Leave fields blank to retain current information.")
                patient['Name'] = input(f"Enter new name (Current: {patient['Name']}): ") or patient['Name']
                patient['Age'] = input(f"Enter new age (Current: {patient['Age']}): ") or patient['Age']
                patient['Gender'] = input(f"Enter new gender (Current: {patient['Gender']}): ") or patient['Gender']
                patient['Phone'] = input(f"Enter new phone (Current: {patient['Phone']}): ") or patient['Phone']
                patient['Address'] = input(f"Enter new address (Current: {patient['Address']}): ") or patient['Address']
                patient['MedicalHistory'] = input(f"Enter new medical history (Current: {patient['MedicalHistory']}): ") or patient['MedicalHistory']
                print("Patient details updated successfully!\n")
                return
        print("Patient not found!\n")

    def delete_patient(self):
        print("\n--- Delete Patient ---")
        patient_id = input("Enter Patient ID to delete: ")
        for patient in self.patients:
            if patient['ID'] == patient_id:
                self.patients.remove(patient)
                print("Patient deleted successfully!\n")
                return
        print("Patient not found!\n")

    def run(self):
        while True:
            print("\n--- Patient Onboarding System ---")
            print("1. Add Patient")
            print("2. View All Patients")
            print("3. Search Patient")
            print("4. Update Patient")
            print("5. Delete Patient")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.view_patients()
            elif choice == '3':
                self.search_patient()
            elif choice == '4':
                self.update_patient()
            elif choice == '5':
                self.delete_patient()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    system = PatientOnboardingSystem()
    system.run()