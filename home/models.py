import uuid

from django.db import models

# Create your models here.

class Student(models.Model):
    MPC="MPC"
    MEG="MEG"
    HEG="HEG"
    MCE="MCE"
    MCB="MCB"
    SUBJECT_CHOICES=[
        
            (MPC,"Math Physic Computer"),
            (MEG,"Math Economy Geography"),
            (MCE,"Math Computer Economy"),
            (MCB,"Math Chemistry Biology")
    ]

    M="MALE"
    F="FEMALE"
    O="OTHER"
    GENDER_CHOICES=[
        
            (M,"Male"),
            (F,"Female"),
            (O,"Other")
        
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    date_ofBirth=models.DateField(auto_created=False)
    subject=models.CharField(choices=SUBJECT_CHOICES,max_length=50,default=MPC)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default=O)
    image=models.ImageField(upload_to="profile_pictures",null=True,blank=True)

    def __str__(self):
        return self.first_name
    
class School(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="school_logoes")

    def __str__(self):
        return self.name
    