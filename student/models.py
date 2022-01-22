from django.db import models

# Create your models here.
class Student(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)
    name = models.CharField(blank=False, max_length=50)
    mobile = models.CharField(blank=True, max_length=10)

    is_email_verified = models.BooleanField(blank=False, default=False)
    is_mobile_verified = models.BooleanField(blank=False, default=False)
    first_login = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email