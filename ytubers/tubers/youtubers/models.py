from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):
    category_choice=(
        ('coding','coding'),
        ('vlog','vlog'),
        ('cooking','cooking'),
        ('unboxing','unboxing')
    )

    camera_choices=(
        ('canon','canon'),
        ('fuji','fuji'),
        ('sony','sony')
    )

    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large')
    )

    name=models.CharField(max_length=500)
    video_url=models.CharField(max_length=500)
    city=models.CharField(max_length=100, default="na")
    age=models.IntegerField()
    price=models.IntegerField()
    height=models.IntegerField()
    subs_count=models.IntegerField()
    photo=models.ImageField(upload_to='media/youtubers/%y/%m')
    description = RichTextField()
    category = models.CharField(max_length=100, choices=category_choice)
    camera_type = models.CharField(max_length=100, choices=camera_choices)
    crew_type = models.CharField(max_length=100, choices=crew_choices)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name