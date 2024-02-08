from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Editor(models.Model):
    title =  models.CharField(max_length=20)
    description = RichTextField()
    
    def __str__(self): 
        return self.title