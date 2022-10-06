from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Books(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title =  models.CharField(max_length=50)
    namber_of_pages = models.PositiveIntegerField(default=1)
def __str__(self):
        return self.title

