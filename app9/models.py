from django.db import models
class CourseTable(models.Model):
    courseno=models.IntegerField(primary_key=True)
    coursename=models.CharField(unique=True,max_length=30)
    def __str__(self):
        return self.coursename
class StudentTable(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    con=models.IntegerField(primary_key=True)
    dob=models.DateField()
    course=models.ManyToManyField(CourseTable)
    gen=models.CharField(max_length=10)
    usrname=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)
class LoginTable(models.Model):
    usrname=models.CharField(max_length=30)
    pas=models.CharField(max_length=40)
    type=models.CharField(max_length=30)
