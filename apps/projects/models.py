from __future__ import unicode_literals
from django.db import models
from apps.login_registration.models import Users

class ProjectsManager(models.Manager):
    def project_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "That's not much of a project"
        if len(postData['description']) < 10:
            errors['description'] = "Could you expand on that?"
        return errors


class Projects(models.Model):
    title = models.CharField(max_length=30, default='New Project') #default: New Project
    description = models.TextField(null=True, default='Description here') #default: Put your information here and stuff
    # img, default smiley
    # teams
    # reviews
    team_name = models.CharField(max_length=30)
    team_code = models.CharField(max_length=30)
    # users
    objects = ProjectsManager()

class Reviews(models.Model):
    user = models.ForeignKey(Users, related_name="reviews")
    project = models.ForeignKey(Projects, related_name="reviews")
    compleation = models.IntegerField(default=0)
    creativity = models.IntegerField(default=0)
    collaberation = models.IntegerField(default=0)
    complexity = models.IntegerField(default=0)
    objects = ProjectsManager()