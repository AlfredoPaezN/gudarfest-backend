from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 100 )
    lastname = models.CharField(max_length= 120)
    email = models.EmailField(max_length= 200)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name
