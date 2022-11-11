from django.db import models

# Create your models here.
class place(models.Model):
    nme = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pix')
    des = models.TextField()

    def __str__(self):
        return self.nme