from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """Model representing a blog post"""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    content = models.TextField(max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-post_date']

    def get_content(self):
        blog_view = self.content.replace('/assets/blog/', 'https://raw.githubusercontent.com/deathvn/deathvn.github.io/master/assets/blog/')
        return blog_view



class BlogAuthor(models.Model):
    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return self.name.username
    
    def get_absolute_url(self):
        return reverse('blog-author', args=[str(self.id)])


class BlogComment(models.Model):
    description = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.description