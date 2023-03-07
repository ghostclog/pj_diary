from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=50)
    post_pass = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



