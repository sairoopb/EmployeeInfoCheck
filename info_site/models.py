from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    p_number = models.BigIntegerField(unique=True)
    adress = models.TextField(max_length=100)
    ed_qualifications = models.TextField(max_length=100)

    def __str__(self):
        return str(self.pk)

class Credential(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username