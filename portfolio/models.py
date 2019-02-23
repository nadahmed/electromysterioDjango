from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class About(models.Model):
    about = models.TextField(verbose_name="About", max_length=500, blank=False, null=False)
    resume = models.FileField(upload_to='uploads/%Y/%m/%d/')
    portfolioURL = models.URLField(blank=False, null=True)
    def __str__(self):
        return 'About'

class Software(models.Model):
    
    name = models.CharField(verbose_name="Skill", unique=True, max_length=50, blank= False, null=False)
    level = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], blank= False, null=False)
    def __str__(self):
        return self.name

class Others(models.Model):
    
    name = models.CharField(verbose_name="Skill", unique=True, max_length=50, blank= False, null=False)
    level = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], blank= False, null=False)
    def __str__(self):
        return self.name

class Hardware(models.Model):
    
    name = models.CharField(verbose_name="Skill", unique=True, max_length=50, blank= False, null=False)
    level = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], blank= False, null=False)
    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    time = models.DateField()
    description = models.CharField(max_length = 250)
    link = models.URLField(verbose_name="Link to project", blank=False, null = True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(verbose_name="Degree", max_length = 100)
    major = models.CharField(verbose_name="Major", max_length=100, blank= True)
    institution = models.CharField(max_length=50)
    institutionURL= models.URLField(blank= True)
    from_year = models.CharField(verbose_name="From", max_length = 10, blank= True)
    to_year = models.CharField(verbose_name="To", max_length = 10)
    CGPA = models.DecimalField(decimal_places = 2, max_digits=3, blank = True, default = 0)
    scale = models.IntegerField(blank= True, default= 0)
    
    def __str__(self):
        return self.institution

class Work(models.Model):
    title = models.CharField(verbose_name="Role", max_length = 50)
    company = models.CharField(verbose_name="Company", max_length=30)
    companyURL= models.URLField(verbose_name="Company website")
    from_year = models.CharField(verbose_name="From", max_length = 20, blank= True)
    to_year = models.CharField(verbose_name="To", max_length = 20)
    description = models.CharField(verbose_name="Company Description", max_length = 250)

    def __str__(self):
        return self.company

class Volunteer(models.Model):
    title = models.CharField(verbose_name="Role", max_length = 50)
    institution = models.CharField(verbose_name="Institution", max_length=30)
    institutionURL= models.URLField(verbose_name="Website")
    from_year = models.CharField(verbose_name="From", max_length = 10, blank= True)
    to_year = models.CharField(verbose_name="To", max_length = 10)
    description = models.CharField(verbose_name="Description", max_length = 250)

    def __str__(self):
        return self.company