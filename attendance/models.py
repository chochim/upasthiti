from django.db import models

DAYS_OF_WEEK = (
	(0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

# Create your models here.
class Days(models.Model):
    day = models.CharField(max_length=8)
    
    def __str__(self):
        return self.day

class Course(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=7)
    prof = models.CharField(max_length=50)
    days = models.ManyToManyField(Days)
    created_dttm = models.DateTimeField('date published')
    
    def __str__(self):
        return self.code


class Student(models.Model):
    name = models.CharField(max_length=50)
    entry_no = models.CharField(max_length=11, blank=False)#2003CS10186
    
    def __str__(self):
        return self.entry_no

class Register(models.Model):
    date = models.DateField(blank=False)
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    present = models.BooleanField(blank=False, default=False)
    time_marked = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __str__(self):
        return self.student.name

class AttendanceCode(models.Model):
    date = models.DateField(blank=False)
    course = models.ForeignKey(Course)
    code = models.CharField(max_length=6, blank=False)
    created_dttm = models.DateTimeField(auto_now=True,auto_now_add=True)
    def __str__(self):
        return str(self.date)+' :: '+self.code



