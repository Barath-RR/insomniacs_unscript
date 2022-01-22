from django.db import models

# Create your models here.
domain = (
    ("Agriculture and Rural Development", "Agriculture and Rural Development"),
    ("Clean Water", "Clean Water"),
    ("Robotics & Drones", "Robotics & Drones"),
    ("Healthcare & Biomedical Devices", "Healthcare & Biomedical Devices"),
    ("Energy / Renewable Energy", "Energy / Renewable Energy"),
    ("Security & Surveillance", "Security & Surveillance"),
    ("Smart Communication", "Smart Communication"),
    ("Smart Vehicles", "Smart Vehicles"),
    ("Software - Mobile App development", "Software - Mobile App development"),
    ("Miscellaneous", "Miscellaneous"),
    ("Software - Web App development", "Software - Web App development"),
    ("Travel and Tourism", "Travel and Tourism"),
    ("Finance", "Finance"),
    ("Life Sciences", "Life Sciences"),
    ("Waste Management", "Waste Management"),
    ("Food Technology", "Food Technology"),
    ("Smart Education", "Smart Education"),
    ("Smart Cities", "Smart Cities"),
    ("Sports and Fitness", "Sports and Fitness"),
    ("Smart Textiles", "Smart Textiles"),
    ("Sustainable Environment", "Sustainable Environment"),

)

class CourseMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, unique=True)
    description = models.TextField(max_length=1000, blank=False)
    file = models.FileField(upload_to='problem_statements/dataset/', blank=True)
    link = models.URLField(max_length=100, blank=True)
    domain_bucket = models.CharField(choices=domain, max_length=50, blank=False)
    prize = models.CharField(max_length=100, blank=False)
    # submitted_by = models.ForeignKey(coursecreator, blank=False, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)
    name = models.CharField(blank=False, max_length=50)
    organization = models.CharField(blank=False, max_length=50)
    country = models.CharField(default="India", blank=False, max_length=30)
    # organization_type = models.CharField(blank=False, max_length=30)
    # state = models.CharField(blank=False, max_length=30)
    mobile = models.CharField(blank=False, max_length=10)
    # city = models.CharField(blank=False, max_length=30)
    designation = models.CharField(blank=False, max_length=50)
    # linked_in = models.CharField(blank=True, max_length=100)
    # department = models.CharField(blank=False, max_length=50)
    idproof = models.FileField(upload_to="teacher/id_proof", blank=False)
    is_email_verified = models.BooleanField(blank=False, default=False)
    is_mobile_verified = models.BooleanField(blank=False, default=False)
    first_login = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email