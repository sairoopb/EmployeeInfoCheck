from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    p_number = models.BigIntegerField()
    adress = models.TextField(max_length=100)
    ed_qualifications = models.TextField(max_length=100)

    def __str__(self):
        return str(self.pk)
