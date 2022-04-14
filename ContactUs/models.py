from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    details = models.CharField(max_length=500)

    def __str__(self):
        return "Input by : " + str(self.name) + " " + str(self.email) + " On : " + str(self.details)