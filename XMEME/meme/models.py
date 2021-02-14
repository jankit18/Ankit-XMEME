from django.db import models


class ContentImage(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)
   

    def __str__(self):
        return self.name + " ("+ str(self.id) + ") "