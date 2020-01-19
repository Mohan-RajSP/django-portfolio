from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to="uploaded_image/")






