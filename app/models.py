from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname
class Student(models.Model):
    Sname=models.ForeignKey(School,on_delete=models.CASCADE)
    Stid=models.IntegerField()
    Stname=models.CharField(max_length=100)

    def __str__(self):
        return  self.Stname