from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class City(models.Model):
    name=models.CharField(max_length=200,unique=True,verbose_name='Shaxar')
    about_city=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Shaxar"
        verbose_name_plural= "Shaxarlar ombori"
        ordering=["name"]
