from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.UserID

class login(models.Model):
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
