from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=250)
    decscription=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self .name


# Create your models here.
