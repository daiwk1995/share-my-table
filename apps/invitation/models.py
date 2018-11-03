import datetime

from django.db import models


# Create your models here.
class MessageModel(models.Model):
    """
    post model
    """
    user = models.ForeignKey("user.UserProfile", related_name="created_user", on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(default=datetime.datetime.now)


class AnswerModel(models.Model):
    """
    Reply post model
    """
    user = models.ForeignKey("user.UserProfile", related_name="answer_user", on_delete=models.CASCADE)
    message = models.ForeignKey("invitation.MessageModel", related_name="message_answered", on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(default=datetime.datetime.now)
    answer_to = models.ForeignKey("invitation.AnswerModel", null=True, blank=True, default=None,
                                  related_name="answer_answered", on_delete=models.CASCADE)
