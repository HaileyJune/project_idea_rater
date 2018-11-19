from django.db import models

class ProjectsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "That's not much of a project"
        if len(postData['description']) < 10:
            errors['description'] = "Could you expand on that?"
        return errors

class CommentsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors['content'] = "You don't have anything to say?"
        elif len(postData['content']) < 3:
            errors['content'] = "You couldn't even say 'nice!'? Say a little more."
        return errors


class Projects(models.Model):
    user = models.ForeignKey(Users, related_name="projects")
    title = models.CharField(max_length=60)
    description = models.TextField(null=True)

    objects = ProjectsManager()

class Reviews(models.Model):
    user = models.ForeignKey(Users, related_name="reviews")
    project = models.ForeignKey(Projects, related_name="reviews")
    compleation =
    creativity = 
    collaberation =
    complexity =

    objects = ReviewsManager()

class Comments(models.Model):
    user = models.ForeignKey(Users, related_name="comments")
    project = models.ForeignKey(Projects, related_name="comments")
    content = models.TextField(null=True)
    
    objects = CommentsManager()