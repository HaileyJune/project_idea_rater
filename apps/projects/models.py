from django.db import models

class ProjectsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "That's not much of a project"
        if len(postData['description']) < 10:
            errors['description'] = "Could you expand on that?"
        return errors

# class CommentsManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['content']) < 1:
#             errors['content'] = "You don't have anything to say?"
#         elif len(postData['content']) < 3:
#             errors['content'] = "You couldn't even say 'nice!'? Say a little more."
#         return errors


class Projects(models.Model):
    title = models.CharField(max_length=60) #default: New Project
    description = models.TextField(null=True) #default: Put your information here and stuff
    # img, default smiley
    objects = ProjectsManager()
    # teams
    # reviews

class Reviews(models.Model):
    user = models.ForeignKey(Users, related_name="reviews")
    project = models.ForeignKey(Projects, related_name="reviews")
    compleation = models.IntegerField(default=0)
    creativity = models.IntegerField(default=0)
    collaberation = models.IntegerField(default=0)
    complexity = models.IntegerField(default=0)

    objects = ReviewsManager()

# class Comments(models.Model):
#     user = models.ForeignKey(Users, related_name="comments")
#     project = models.ForeignKey(Projects, related_name="comments")
#     content = models.TextField(null=True)
    
#     objects = CommentsManager()

class Teams(models.Model):
    team_name = models.CharField(max_length=60)
    team_code = models.CharField(max_length=60)
    project = models.ForeignKey(Projects, related_name="team")
    # users
