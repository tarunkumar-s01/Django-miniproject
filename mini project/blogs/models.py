from django.db import models

# Create your models here.
class blog(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    rating=models.IntegerField()
    image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return f'name:{self.name} age:{self.description}'
    

class form(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    text=models.TextField(max_length=100,null=True)

