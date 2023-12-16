from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    publication_year = models.IntegerField(null=False)
    isbn = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_json_attrs(cls):
        return ['title', 'author', 'publication_year', 'isbn']