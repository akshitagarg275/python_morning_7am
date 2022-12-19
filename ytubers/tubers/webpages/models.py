from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    btn_text = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/slider/%y/%M")

    def __str__(self):
        return self.title

class Team(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    role=models.CharField(max_length=100,default='NA')
    fb_link=models.CharField(max_length=100)
    insta_link=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    photo=models.ImageField(upload_to='media/team/%y/%m/%d')

    def __str__(self):
        return self.first_name 