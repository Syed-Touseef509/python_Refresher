import os
import csv
import asyncio
import logging
from student import Student
from utils import InvalidRecordError, log_execution
from datetime import datetime
from dotenv import load_dotenv

# Load config from .env
load_dotenv()
CSV_FILE = os.getenv("CSV_FILE")
print("CSV file path:", CSV_FILE)
REPORT_DIR = os.getenv("REPORT_DIR")

# Async function to load students
@log_execution
async def load_students():
    students = []
    try:
        with open(CSV_FILE, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    if not row['student_id'] or not row['grade']:
                        raise InvalidRecordError(f"Invalid record: {row}")
                    student = Student(
                        row['student_id'],
                        row['name'],
                        row['grade'],
                        row['fees_paid'],
                        row['submission_date']
                    )
                    students.append(student)
                except InvalidRecordError as e:
                    logging.error(e)
    except FileNotFoundError:
        logging.error(f"{CSV_FILE} not found!")
    return students

# Async function to process student records
async def process_student(student):
    student.check_fail()
    student.calculate_late_fine()

# Async function to generate report
@log_execution
async def generate_report(students):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"{REPORT_DIR}/report_{timestamp}.csv"
    with open(report_file, 'w', newline='') as f:
        fieldnames = ['ID', 'Name', 'Grade', 'Failed', 'Late Fine']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow({
                'ID': s.student_id,
                'Name': s.name,
                'Grade': s.grade,
                'Failed': s.failed,
                'Late Fine': s.late_fine
            })
    print(f"Report generated: {report_file}")

# Main async function
async def main():
    students = await load_students()
    await asyncio.gather(*(process_student(s) for s in students))
    await generate_report(students)

if __name__ == "__main__":
    asyncio.run(main())