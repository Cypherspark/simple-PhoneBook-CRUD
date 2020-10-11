from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, null =True, blank=True, unique=True)

    def __str__(self):
        return f"{self.tag_name}"


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=17, blank=True, null= True)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone_number}"


class PhoneBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    description = models.CharField(max_length=255, blank=True, null= True)

    def __str__(self):
        return f"{self.description}"


class Contact(models.Model):
    phone_book = models.ForeignKey("PhoneBook", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null= True)
    last_name = models.CharField(max_length=255, blank=True, null= True)
    nick_name = models.CharField(max_length=50, blank=True, null= True)
    numbers_list = models.ManyToManyField("PhoneNumber")

    def __str__(self):
        return f"{self.id}"





    
