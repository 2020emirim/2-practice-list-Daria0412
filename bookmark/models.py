from django.db import models

class Bookmark(models.model):
    site_name = models.CharField(max_length = 20)
    url = models.URLField('site URL')
    k

    
    