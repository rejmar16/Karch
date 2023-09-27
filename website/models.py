from django.db import models

from tinymce import models as tinymce_models
# Create your models here.

PROJECTS_TYPES = (
    ('RD', ('Rodinne domy')),
    ('INTER', ('Interiery')),
    ('JINE', ('Jine')),
)

class Project(models.Model):
    name = models.CharField(max_length=200)
    screen = models.ImageField(upload_to = 'screen/', default = 'screen_folder/None/no-img.jpg')
    text = tinymce_models.HTMLField(default='NA')
    type = models.CharField(max_length=10, blank= True, null=True, choices=PROJECTS_TYPES)
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    def __str__(self):
        return self.name

class Project_Photo(models.Model):
    rodinny_dum = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo_name = models.CharField(max_length=200)
    number = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to = 'photo_folder/', default = 'photo_folder/None/no-img.jpg')

    def __str__(self):
        return self.photo_name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    text = tinymce_models.HTMLField(default='NA',max_length=1000)
    photo = models.ImageField(upload_to = 'photo/', default = 'photo/None/no-img.jpg')

    def __srt__(self):
        return self.first_name
