# from ast import mod
# from random import choices
from contextlib import nullcontext
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
# from django.forms import CharField

class Db_admin(models.Model):
    user_name = models.CharField(max_length=30,primary_key=True)
    user_password = models.CharField(max_length=20)


class Company(models.Model):
    admin_user_name = models.ForeignKey(Db_admin,on_delete=models.SET_DEFAULT,default=None)
    company_registrationno = models.IntegerField(primary_key=True)
    company_password = models.CharField(max_length=30,unique=True)
    company_name = models.CharField(max_length=100)
    company_location =models.CharField(max_length=20)
    company_description = models.TextField(null=True)


class postajob(models.Model):
    related_company = models.ForeignKey(Company,on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=120)
    job_vacancynum = models.CharField(max_length=100)
    job_emailaddress = models.EmailField()
    job_startingdate = models.DateField()
    job_endingdate = models.DateField()
    job_experience = models.CharField(max_length=30)
    job_duration = models.CharField(max_length=100)
    job_salary = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15)
    job_noofoppurtunity = models.IntegerField()
    job_location = models.CharField(max_length=30)
    job_communicationskills = models.CharField(max_length=40)
    job_degree = models.CharField(max_length=30,null = True)
    job_field = models.CharField(max_length=40,null=True)
    job_seconddegree = models.CharField(max_length=30,null=True)
    job_secondfield = models.CharField(max_length=40,null = True)
    job_gender = models.CharField(max_length=10)
    job_educationalskillfirst = models.CharField(max_length=100,null=True)
    job_educationalskillsecond = models.CharField(max_length=100,null=True)
    job_educationalskillthird = models.CharField(max_length=100,null=True)
    job_educationalskillfourth = models.CharField(max_length=100,null=True)
    job_computerskillfirst = models.CharField(max_length=100,null=True)
    job_computerskillsecond = models.CharField(max_length=100,null=True)
    job_computerskillthird = models.CharField(max_length=100,null=True)
    job_firstlanguage = models.CharField(max_length=100,null = True)
    job_firstknowpercentage = models.IntegerField(null = True)
    job_secondlanguage = models.CharField(max_length=100,null=True)
    job_secondknowpercentage = models.IntegerField(null=True)
    job_thirdlanguage = models.CharField(max_length=100,null=True)
    job_thirdknowpercentage = models.IntegerField(null=True)
    job_descriptoin = models.TextField(null = True)
    job_responsibilities = models.TextField(null = True)




class Applier(models.Model):
    Job_id = models.ForeignKey(postajob,on_delete=models.CASCADE)
    applierusername = models.CharField(max_length=30)
    applieremail = models.EmailField()
    applierphoneno = models.IntegerField(null = True)
    applieridentityno = models.IntegerField()
    applierdateofbirth = models.DateField()
    appliergender = models.CharField(max_length=10)
    applierorignlocation = models.CharField(max_length=30)
    appliercurrentlocation = models.CharField(max_length=30)
    applierdegree = models.CharField(max_length=30)
    applierfield = models.CharField(max_length=40)
    applierseconddegree = models.CharField(max_length=30,null = True)
    appliersecondfield = models.CharField(max_length=40,null=True)
    appliercommunicationskills = models.CharField(max_length=40)
    applierexperience = models.CharField(max_length=30)
    appliereducationalskillfirst = models.CharField(max_length=100,null=True)
    appliereducationalskillsecond = models.CharField(max_length=100,null=True)
    appliereducationalskillthird = models.CharField(max_length=100,null=True)
    appliereducationalskillfourth = models.CharField(max_length=100,null=True)
    appliercomputerskillfirst = models.CharField(max_length=100,null=True)
    appliercomputerskillsecond = models.CharField(max_length=100,null=True)
    appliercomputerskillthird = models.CharField(max_length=100,null=True)
    applierfirstlanguage = models.CharField(max_length=100,null=True)
    applierfirstknowpercentage = models.IntegerField(null=True)
    appliersecondlanguage = models.CharField(max_length=100,null=True)
    appliersecondknowpercentage = models.IntegerField(null=True)
    applierthirdlanguage = models.CharField(max_length=100,null=True)
    applierthirdknowpercentage = models.IntegerField(null=True)
    aplirdescription = models.TextField(null = True)

