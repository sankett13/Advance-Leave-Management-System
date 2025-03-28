import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Adv_Leave_Management_System.settings')  # Replace 'your_project'
django.setup()

from main.models import StudentBasicDetail, StudentContactDetail, LeaveHistory, FacultyDetail, Department # Replace your_app

fake = Faker()

# Create fake Departments
departments = []
for _ in range(5):
    dept = Department.objects.create(dep_name=fake.job())
    departments.append(dept)

# Create fake FacultyDetails
faculties = []
for _ in range(10):
    faculty = FacultyDetail.objects.create(
        name=fake.name(),
        department=fake.random_element(elements=departments),
        Batch_Year=fake.year(),
        is_incharge=fake.boolean()
    )
    faculties.append(faculty)

# Create fake StudentBasicDetails
students = []
for _ in range(20):
    student = StudentBasicDetail.objects.create(
        name=fake.name(),
        enrollment_no=fake.random_number(digits=8),
        sp_id=fake.random_number(digits=6),
        department=fake.random_element(elements=departments),
        password=fake.password(),
        FA=fake.random_element(elements=faculties)
    )
    students.append(student)

# Create fake StudentContactDetails
for student in students:
    StudentContactDetail.objects.create(
        StudentID=student,
        PhoneNumber=fake.random_number(digits=10),
        Email=fake.email(),
        Address=fake.address(),
        City=fake.city(),
        Pincode=fake.postcode(),
        Hostel_Block=fake.random_element(elements=['A', 'B', 'C', 'D']),
        Room_No=fake.random_number(digits=3),
        Parent_No=fake.random_number(digits=10),
        Parent_Email=fake.email() if fake.boolean() else None,  # Some Parent_Emails might be None
    )

# Create fake LeaveHistory
for student in students:
    LeaveHistory.objects.create(
        student_id=student,
        start_date=fake.date_between(start_date='-1y', end_date='today'),
        end_date=fake.date_between(start_date='-1y', end_date='today'),
        no_of_days=fake.random_number(digits=2),
        reason=fake.sentence(),
        place_to_visit=fake.city(),
        status_parent=fake.boolean(),
        status_fa=fake.boolean(),
        status_incharge=fake.boolean()
    )

print("Successfully populated database with fake data.")