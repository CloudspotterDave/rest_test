from django.db import models

class Upload(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey('auth.User', related_name='uploads')
  pic_url = models.TextField()
