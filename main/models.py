from django.db import models

class StudentBasicDetails(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.IntegerField()  
    sp_id = models.IntegerField()        
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)    
    password = models.CharField(max_length=50)
    FA = models.ForeignKey('FacultyDetails', on_delete=models.CASCADE)         

    def __str__(self):
        return f"{self.name} - {self.enrollment_no}-{self.department}-{self.FA}"

class StudentContactDetails(models.Model):
    StudentID = models.ForeignKey('StudentBasicDetails', on_delete=models.CASCADE) 
    PhoneNumber = models.CharField(max_length=10) 
    Email = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=6)
    Hostel_Block = models.CharField(max_length=1)
    Room_No = models.CharField(max_length=3)       
    Parent_No = models.CharField(max_length=20)    
    Parent_Email = models.CharField(max_length=255)

    def __str__(self):
        return str(self.StudentID)

class LeaveHistory(models.Model):
    student_id = models.CharField(max_length=20)     
    start_date = models.CharField(max_length=20)     
    end_date = models.CharField(max_length=20)      
    no_of_days = models.CharField(max_length=20)   
    reason = models.CharField(max_length=20)       
    place_to_visit = models.CharField(max_length=20)
    status_parent = models.BooleanField()
    status_fa = models.BooleanField()
    status_incharge = models.BooleanField()

    def __str__(self):
        return str(self.student_id)

class Departments(models.Model):
    dep_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dep_name

class FacultyDetails(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)    
    Batch_Year = models.CharField(max_length=20)    
    is_incharge = models.BooleanField()

    def __str__(self):
        return self.name