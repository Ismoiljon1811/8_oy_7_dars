from django.db import models

class Header(models.Model):
    image = models.ImageField(upload_to="media")
    phone_number = models.CharField(max_length = 13)
    telegram_link = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.phone_number
    
class HeaderBody(models.Model):
    image = models.ImageField(upload_to="media")
    travel_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.travel_name
    

class Tariffs(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    duration = models.IntegerField()
    eating = models.IntegerField()
    viza = models.BooleanField()
    medical_care = models.CharField(max_length = 5)
    experience = models.CharField(max_length = 100)
    water_zam_zam = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

