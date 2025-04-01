from django.db import models

class StudentBasicDetail(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.IntegerField()  
    sp_id = models.IntegerField()        
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    Batch_Year = models.CharField(max_length=20)    
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.enrollment_no}-{self.department}-{self.Batch_Year}"

class StudentContactDetail(models.Model):
    StudentID = models.ForeignKey('StudentBasicDetail', on_delete=models.CASCADE) 
    PhoneNumber = models.IntegerField()
    Email = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    Hostel_Block = models.CharField(max_length=1)
    Room_No = models.IntegerField()   
    Parent_No = models.IntegerField()
    Parent_Email = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return str(self.StudentID)

from django.db import models

class LeaveHistory(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    student_id = models.ForeignKey('StudentBasicDetail', on_delete=models.CASCADE)
    start_date = models.DateField(max_length=20)
    end_date = models.DateField(max_length=20)
    no_of_days = models.IntegerField()
    reason = models.CharField(max_length=20)
    place_to_visit = models.CharField(max_length=20)
    status_parent = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    status_fa = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    status_incharge = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.student_id)


class FacultyDetail(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)    
    Batch_Year = models.CharField(max_length=20)
    fp_id = models.IntegerField()
    password = models.CharField(max_length=50)    
    is_incharge = models.BooleanField()

    def __str__(self):
        return self.name


class Department(models.Model):
    dep_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dep_name