from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import date

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    

class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_post')
    description = models.TextField()
    created = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title + "-" + str(self.created))
        return super().save(*args, **kwargs)


class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog
    
