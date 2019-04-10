from django.db import models
from django.urls import reverse

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=264)
    location=models.CharField(max_length=264)
    principal=models.CharField(max_length=264)

    def  __str__(self):
        return self.name
    def get_absolute_url(self): #this will work when we clik n submit button on student_form and this fucntion will show the detail of newly created school

        return reverse('detail',kwargs={'pk':self.pk})


class students(models.Model):
    name=models.CharField(max_length=264)
    school=models.ForeignKey(school,related_name='students',on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

