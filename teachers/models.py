from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(unique=True,max_length=15)
    image = models.ImageField(upload_to="teacher/",blank=True,null=True)


    def __str__(self):
        return (f"{self.name}-{self.subject}")