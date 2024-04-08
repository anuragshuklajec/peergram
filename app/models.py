from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class CustomUser(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20,unique=True)
    email = models.EmailField(unique=True)
    password = models.EmailField()

    def clean(self):
        super().clean()
        if not self.email:
            raise ValidationError("Email field is required")
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError("Invalid email address")
        
class Domain(models.Model):
    name = models.CharField(max_length = 20,unique=True)

class Tag(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,unique=True)

class UserChoice(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)


    