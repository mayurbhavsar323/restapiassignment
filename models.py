from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name 



class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='art')