from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    propic = models.ImageField(upload_to='Profilepic', null=True)

    def __str__(self):
        return str(self.name)