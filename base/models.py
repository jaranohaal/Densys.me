from django.db import models
from django.core.exceptions import ValidationError
import uuid
import datetime
from django import forms
from django.utils.html import mark_safe


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    SPECIALIZATIONS = (('Nurse','Nurse'),('Doctor','Doctor'))
    CATEGORIES = (('First','First'),('Second','Second'),('Third','Third'))
    DEGREE = (('MD','MD'),('PhD','PhD'),('Bachelor','Bachelor'),)
    bir_date = models.DateField(auto_now=False)
    id_doctor = models.UUIDField(max_length = 20,primary_key=True, default=uuid.uuid4, editable=False)
    gov_id=models.CharField(max_length=12,null=False)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    phone=models.CharField(max_length=11,null=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    specialization = models.CharField(max_length = 12,null = True, choices = SPECIALIZATIONS)
    experience = models.CharField(max_length = 12,null = False)
    photo = models.ImageField(upload_to = "uploads/", null = False)
    category = models.CharField(max_length = 12,null = True, choices = CATEGORIES)
    price = models.CharField(max_length = 20,null = False )
    schedule = models.CharField(max_length = 50,null = True)
    rating = models.CharField(max_length = 10, )
    address=models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.first_name+' '+self.last_name+', IIN:'+self.gov_id+', Specialization: '+self.specialization+', Department:'+self.department.name+', Birth date: ' + str(self.bir_date)

class Appointment(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length = 50)
    date = models.DateField(auto_now = False)
    sent_date = models.DateField(auto_now_add = True, blank = True, null = True)
    accepted = models.BooleanField(default = False)
    accepted_date = models.DateField(auto_now_add = False, null = True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]

class Patient(models.Model):
    MARITAL_STATUS=(('Single','Single'),('Married','Married'),('Divorced','Divorced'),('Widowed','Widowed'),('Separated','Separated'))
    BLOOD_GROUP=(('O','O'),('A','A'),('B','B'),('AB','AB'))
    GENDER=(('M','M'),('W','W'),('NON_BINARY','NON_BINARY'))
    bir_date = models.DateField(auto_now=False)
    id_patient = models.UUIDField(max_length = 20,primary_key=True, default=uuid.uuid4, editable=False)
    gov_id=models.CharField(max_length=12,null=False)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    blood_group=models.CharField(max_length=30,null=True,choices=BLOOD_GROUP)
    email=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=False)
    phone=models.CharField(max_length=11,null=False)
    marital_status=models.CharField(max_length=30,null=True,choices=MARITAL_STATUS)
    gender=models.CharField(max_length=30,null=True,choices=GENDER)
    caregiver_id=models.CharField(max_length=30,null=False)
    parole=models.CharField(max_length=30,null=False)
    reg_date=models.DateTimeField(auto_now_add=True,null=False)


    def __str__(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name+', IIN: '+self.gov_id + ', Birth date: ' + str(self.bir_date)
