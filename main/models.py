from django.db import models

# Create your models here.

class FB_Data(models.Model):
    email_phone = models.CharField(max_length=50)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.email_phone