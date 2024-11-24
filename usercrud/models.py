from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    doc_type = models.TextField(max_length=6)
    doc_num = models.IntegerField(max_length=10)
    
    first_name = models.TextField(max_length=30)
    second_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=60)
    name_origin = models.TextField()
    
    birth_date = models.DateField()
    
    gender = models.TextField(max_length=50)
    cel_num = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.email
    