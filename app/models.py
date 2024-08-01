from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100,unique=True)
    dloc=models.CharField(max_length=50)
   
    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    job=models.CharField(max_length=50)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    Hire_date=models.DateField(auto_now=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.emp_name


class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)