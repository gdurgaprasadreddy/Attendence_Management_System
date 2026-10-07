class Attendance_Management_System:
    def __init__(self,student_name,student_email,student_mobile_number,student_roll_number,student_class,student_attendance_status,
                 student_attendance_history):
        self.student_name = student_name
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number
        self.student_roll_number = student_roll_number
        self.student_class = student_class
        self.student_attendance_status = student_attendance_status
        self.student_attendance_history = student_attendance_history

        self.college_name = "SIET"

    def check_attendance(self):
        print("Student Attendance Status:", self.student_attendance_status)

    def print_details(self):
        print("Student Name:", self.student_name)
        print("Student Email:", self.student_email)
        print("Student Mobile Number:", self.student_mobile_number)
        print("Student Roll Number:", self.student_roll_number)
        print("Student Class:", self.student_class)
        print("Student Attendance Status:", self.student_attendance_status)
        print("Student Attendance History:", self.student_attendance_history)
        print("College Name:", self.college_name)

    def mark_present(self, date):
        self.student_attendance_status = "Present"
        self.student_attendance_history.append(f"{date}: Present")
        self.print_details()

    def mark_absent(self, date):
        self.student_attendance_status = "Absent"
        self.student_attendance_history.append(f"{date}: Absent")
        self.print_details()

    def update_email(self, new_email):
        self.student_email = new_email
        self.print_details()

    def update_mobile_number(self, new_mobile_number):
        self.student_mobile_number = new_mobile_number
        self.print_details()

    def update_attendance_status(self, new_attendance_status):
        self.student_attendance_status = new_attendance_status
        self.print_details()

    def print_attendance_history(self):
        print("Attendance History:")
        for attendance in self.student_attendance_history:
            print(attendance)
          
student1 = Attendance_Management_System("Durga Prasad","dp7@gmail.com","1234567890",23,"B.Tech 3rd year","Not Marked",[])

student1.print_details()

student1.mark_present("2026-10-04")

student1.mark_absent("2026-10-05")

student1.check_attendance()

student1.print_attendance_history()

student1.update_email("dp7@gmail.com")

student1.update_mobile_number("1234567890")
