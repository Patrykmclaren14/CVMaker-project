from random import choices
from django.db import models

# Create your models here.



class Characteristic(models.Model):
    name = models.CharField(max_length=200)

class Skill(models.Model):
    name = models.CharField(max_length=200)
    level_choices = models.IntegerChoices('Level', [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

class Language(models.Model):
    name = models.CharField(max_length=200)
    level_choices = models.IntegerChoices('Level', [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

class Education(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date = models.DateField()

class Experience(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date = models.DateField()



class Data(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='uploads/', blank=False)
    phone = models.SmallIntegerField(max_length=20)
    aboutMe = models.TextField(max_length=2500)
    characteristics = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

