from django.db import models

class dept(models.Model):
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=150)

class emp(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=150)
    emp_salary = models.IntegerField()
    dept_id = models.ForeignKey(dept,on_delete=models.CASCADE)