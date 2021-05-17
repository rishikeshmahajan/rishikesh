from django.db import models

class ProductModel(models.Model):
    pno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    price=models.FloatField()
    quantity=models.IntegerField()


class EmployeeModel(models.Model):
    eno=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
