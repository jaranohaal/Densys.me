from django.db import models
from django.core.exceptions import ValidationError
import uuid
import datetime
from django import forms

#Functions
def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

#Tuples


# Create your models here.

class Doctor(models.Model):
    DEPARTMENTS = (('medicine','medicine'),('surgery','surgery'),('gynecology','gynecology'),('obstetrics','obstetrics'),('pediatrics','pediatrics'),('radiology','radiology'),('eye','eye'),('ENT','ENT'),('dental','dental'),('orthopedics','orthopedics'),('neurology','neurology'),('cardiology','cardiology'),('psychiatry','psychiatry'),('skin','skin'))
    SPECIALIZATIONS = (('nurse','nurse'),('doctor','doctor'))
    CATEGORIES = (('first','first'),('second','second'),('third','third'))
    DEGREE = (('MD','MD'),('PhD','PhD'),('Bachelor','Bachelor'),)

    bir_date = models.CharField(max_length=12,null=False)

    id_doctor = models.UUIDField(max_length = 20,primary_key=True, default=uuid.uuid4, editable=False)
    gov_id=models.CharField(max_length=12,null=False)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    phone=models.CharField(max_length=11,null=False)
    department = models.CharField(max_length = 12,null = True, choices = DEPARTMENTS)
    specialization = models.CharField(max_length = 12,null = True, choices = SPECIALIZATIONS)
    experience = models.CharField(max_length = 12,null = False)
    photo = models.ImageField(upload_to = "uploads/", null = False)
    category = models.CharField(max_length = 12,null = True, choices = CATEGORIES)
    price = models.CharField(max_length = 20,null = False )
    schedule = models.CharField(max_length = 50,null = True)
    rating = models.CharField(max_length = 10, )
    address=models.CharField(max_length=200,null=False)

class Patient(models.Model):
    MARITAL_STATUS=(('Single','Single'),('Married','Married'),('Divorced','Divorced'),('Widowed','Widowed'),('Separated','Separated'))
    BLOOD_GROUP=(('O','O'),('A','A'),('B','B'),('AB','AB'))
    GENDER=(('M','M'),('W','W'),('NON_BINARY','NON_BINARY'))

    bir_date = models.CharField(max_length=12,null=False)

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


   # def __str__(self):
    #    return
