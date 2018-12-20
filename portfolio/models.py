from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
    name = models.CharField(_("Skill"), unique=True, max_length=50, blank= False, null=False)
    level = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], blank= False, null=False)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    time = models.DateField()
    description = models.CharField(max_length = 250)
    link = models.URLField(_("Link to project"), blank=False, null = True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(_("Degree"), max_length = 100)
    major = models.CharField(_("Major"), max_length=50)
    institution = models.CharField(max_length=50)
    institutionURL= models.URLField()
    from_year = models.DateField(_("From"))
    to_year = models.DateField(_("To"))

class Work(models.Model):
    title = models.CharField(_("Role"), max_length = 50)
    company = models.CharField(_("Company"), max_length=30)
    companyURL= models.URLField(_("Company website"))
    from_year = models.DateField(_("From"))
    to_year = models.DateField(_("To"))
    description = models.CharField(_("Company Description"), max_length = 250)