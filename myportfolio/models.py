from django.db import models

# Create your models here.
# class Hire(models.Model):
#     title = models.CharField(blank=False, null=False,max_length=100)
#     phone_number = models.CharField(blank=False, null=False,max_length=255)
#     subject = models.TextField()
#     email = models.EmailField(blank=False)
#     message = models.CharField(max_length=255)
#     data_created = models.DateField() 

#     def __str__(self) :
#         return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
   

    def __str__(self) :
        return self.title

class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    
   

    def __str__(self) :
        return self.title

EDUCATION_LEVEL = (
    ('Primary','Primary'),
    ('Seconadry','Secondary'),
    ('Tertiary','Tertiary'),
    ('Master','Master'),
    ('Phd','Phd')
)
class Education(models.Model):
     title = models.CharField(max_length=100)
     education_level = models.CharField(max_length=100, choices=EDUCATION_LEVEL)
     description = models.TextField()

     start_date = models.DateField()
     end_date = models.DateField(blank=True,null=True)


class Post(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=400)
    date = models.DateField(blank=True,null=True)
   

    def __str__(self) :
        return self.name