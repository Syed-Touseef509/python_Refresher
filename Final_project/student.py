from datetime import datetime

class Student:
    def __init__(self, student_id, name, grade, fees_paid, submission_date):
        self.student_id = student_id
        self.name = name
        self.grade = int(grade)
        self.fees_paid = float(fees_paid)
        self.submission_date = submission_date
        self.failed = False
        self.late_fine = 0

    def check_fail(self):
        self.failed = self.grade < 40
        return self.failed

    def calculate_late_fine(self, due_date="2026-03-05"):
        fmt = "%Y-%m-%d"
        days_late = (datetime.strptime(self.submission_date, fmt) -
                     datetime.strptime(due_date, fmt)).days
        self.late_fine = max(0, days_late * 5)  # 5 units per late day
        return self.late_fine