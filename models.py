# from django.db import models

# # Create your models here.
from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        if len(postData['birth_year']) < 8:
            errors["birth_year"] = "Birth year should be at least 8 characters"
        if len(postData['email']) < 5:
            errors["email"] = "email should be at least 5 characters"
        if len(postData['password']) < 6:
            errors["password"] = "Password should be at least 6 characters"
        if len(postData['confirm_pw']) < 6:
            errors["confirm_pw"] = "Password should be at least 6 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_year = models.DateTimeField()
    email = models.CharField(max_length=255)
    password =  models.CharField(max_length=255)
    confirm_pw =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    messager = models.ForeignKey(User, related_name="messages_made", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    commentor = models.ForeignKey(User, related_name="comments_made", on_delete=models.CASCADE)
    post = models.ForeignKey(Message, related_name="post_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


