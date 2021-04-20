from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class City(models.Model):
    name=models.CharField(max_length=200,unique=True,verbose_name='Shaxar')
    shahar_haqida_qisqa = models.CharField(max_length=1000)
    about_city=RichTextUploadingField(blank=True,null=True)
    image = models.ImageField(blank=True, null=True, upload_to='city_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Shaxar"
        verbose_name_plural= "Shaxarlar ombori"
        ordering=["name"]
