from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,

    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name= models.CharField(max_length=100, unique=True)

    def __str__(self):
         return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length = 200, blank=True)
    slug = models.SlugField(max_length= 200, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length = 200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(
        Profile, on_delete=models.PROTECT
    ) 
    tags = models.ManyToManyField(Tag, blank=True)

class Meta:
    ordering = ['-date_created']      



# Create your models here.
