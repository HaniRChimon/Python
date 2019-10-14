from __future__ import unicode_literals
from django.db import models
import re

class BookManager(models.Manager):
    def Book_Validator (self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["titleerror"] = "Book Title is Too short!!"
        elif len(postData['desc']) < 10:
            errors["descerror"] = "Description MUST be 10 characters long!!!"
        return errors




class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = models.Manager()
    objects = BookManager()


class Author (models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = models.Manager()

