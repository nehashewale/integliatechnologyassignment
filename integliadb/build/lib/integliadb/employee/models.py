from django.db import models
    

class Employee(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=30,unique=True)
    manager = models.ForeignKey("Employee", default=None,on_delete=models.CASCADE, null=True, related_name="employee_manager")

class Vacation(models.Model):
    #  "approved", "rejected", "pending”
    status = models.CharField(max_length=20)
    resolved_by = models.ForeignKey(Employee,null=True,on_delete=models.CASCADE,related_name='resolved_by')
    request_created_at = models.DateTimeField(auto_now_add=True)
    vacation_start_date = models.DateTimeField() 
    vacation_end_date = models.DateTimeField()
    author = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='author')
