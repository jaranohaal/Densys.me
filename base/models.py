from django.db import models
from django.core.exceptions import ValidationError


#Functions
def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

#Tuples


# Create your models here.
class Patient(models.Model):
    MARITAL_STATUS=(('Single','Single'),('Married','Married'),('Divorced','Divorced'),('Widowed','Widowed'),('Separated','Separated'))
    BLOOD_GROUP=(('O','O'),('A','A'),('B','B'),('AB','AB'))
    GENDER=(('M','M'),('W','W'),('NON_BINARY','NON_BINARY'))

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
