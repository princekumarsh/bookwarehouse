from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=255 )
    email = models.CharField( max_length=255)
    mobile = models.CharField( max_length=255)
    password = models.CharField( max_length=255)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name 
    
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField( max_length=255 , null = True)
    name = models.CharField( max_length=255 )
    desc = models.CharField( max_length=255)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name 