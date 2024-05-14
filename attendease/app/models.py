from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2,'COORDINATOR'),
        (3, 'FACULTY'),
        (4, 'STUDENT'),
    )

    user_type = models.CharField(choices=USER, max_length=50)



class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

class Session_Year(models.Model):
    session_year_start = models.CharField(max_length=100)
    session_year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_year_start + " To " + self.session_year_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # first_name=models.CharField(max_length=100)
    # last_name=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    # subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    branch_id = models.ForeignKey(Branch,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    enrolment_no = models.CharField(max_length=100)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Faculty(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Coordinator(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    branch_id = models.ForeignKey(Branch,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code =  models.CharField(max_length=100)
    branch_id = models.ForeignKey(Branch,on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name +" "+ "(" + self.subject_code + ")"

class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_data = models.DateField()
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name

class Attendance_Report(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name
