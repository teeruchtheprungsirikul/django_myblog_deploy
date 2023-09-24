from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    
    def __str__(self) :
        # return self.name
        # return '{} {}.format(self.first_name, self.last_name)'
        return f'{self.first_name} {self.last_name}'

class Blog(models.Model):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types
    # Django model-field-types
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_pic = models.ImageField(upload_to="featured_images", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    """
    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # obj = Blog.objects.get(id=1)
        # set something
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        # obj.save()
        # do another something
    """ 
    
    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        
class Contact(models.Model):
    subject = models.CharField(max_length=120)
    sender = models.CharField(max_length=80)
    email = models.EmailField()
    detail = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.subject
    

    
    
