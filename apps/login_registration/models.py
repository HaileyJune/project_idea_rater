from django.shortcuts import render, redirect
from django.db import models
import re
import bcrypt
# Create your models here.
class UsersManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "That's a suspiciously short name."
        if len(postData['lname']) < 2:
            errors['lname'] = "Write out your full last name, please."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Real Emails Please"
        # also don't allow them to make multiple accounts with the same email
        if len(Users.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "You already have an account!"
        if len(postData['password']) < 8:
            errors['password'] = "Your password is too whimpy."
        if postData['password'] != postData['confirm']:
            errors['confim'] = "You just set the password, how did you get it wrong?"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = Users.objects.filter(email=postData['email'])
        if len(user) < 1:
            errors['email'] = "I've never met you before."
        elif len(user) > 1:
            errors['email'] = "How did you make multiple accounts? Stop?"
        elif len(user) == 1:
            user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.passhash.encode()):
                errors['password'] = "You guessed wrong."
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    passhash = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()