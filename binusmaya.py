class Binusmaya:
    def __init__(self):
        self.Lecturers= []  
        self.Classes= []  
        self.Schedules= [] 

    #add lecturer data
    def add_lecturer(self, name: str, subject: str, lecturerID: str):

        for lecturer in self.Lecturers:
            if lecturer['subject'] == subject:
                print(f"Error: A lecturer is already assigned to {subject}.")
                return
        #add lecturer data as dictionary
        self.Lecturers.append({
            'name': name,
            'subject': subject,
            'lecturerID': lecturerID
        })
        print(f"Lecturer {name} added successfully.")

    #remove lecturer data by lecturerID
    def remove_lecturer(self, lecturerID: str):
        for lecturer in self.Lecturers:
            if lecturer['lecturerID'] == lecturerID:
                self.Lecturers.remove(lecturer)
                print(f"Lecturer with ID {lecturerID} removed successfully.")
                return
        print(f"Error: Lecturer with ID {lecturerID} not found.")

    #add a class code
    def add_class(self, class_code: str):
        if class_code in self.Classes:
            print(f"Error: Class code {class_code} already exists.")
            return
        self.Classes.append(class_code)
        print(f"Class code {class_code} added successfully.")

    # Method to remove a class code
    def remove_class(self, class_code: str):
        if class_code in self.Classes:
            self.Classes.remove(class_code)
            print(f"Class code {class_code} removed successfully.")
        else:
            print(f"Error: Class code {class_code} not found.")

    # Method to add a schedule
    def add_schedule(self, class_code: str, time: str, subject: str):
        # Check if subject exists in Lecturers
        lecturer_name= None
        for lecturer in self.Lecturers:
            if lecturer['subject'] == subject:
                lecturer_name= lecturer['name']
                break
        
        if lecturer_name is None:
            print(f"Error: No lecturer found for subject {subject}.")
            return

        # Create a tuple and append it to the Schedules list
        schedule= (time, class_code, subject, lecturer_name)
        self.Schedules.append(schedule)
        print(f"Schedule for class {class_code} added successfully.")

