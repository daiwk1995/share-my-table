import datetime

from django.db import models


# Create message model
class MessageModel(models.Model):
    """
    post model
    """
    user = models.ForeignKey("user.UserProfile", related_name="created_user", on_delete=models.CASCADE,
                             help_text="the user who post")
    content = models.TextField(help_text="post content")
    created_time = models.DateTimeField(default=datetime.datetime.now, help_text="post time")

#create answer model
class AnswerModel(models.Model):
    """
    Answer model
    """
    user = models.ForeignKey("user.UserProfile", related_name="answer_user", on_delete=models.CASCADE,
                             help_text="the user who reply the post")
    message = models.ForeignKey("invitation.MessageModel", related_name="message_answered", on_delete=models.CASCADE,
                                help_text="the original post")
    content = models.TextField(help_text="reply content")
    created_time = models.DateTimeField(default=datetime.datetime.now, help_text="reply time")
    answer_to = models.ForeignKey("invitation.AnswerModel", null=True, blank=True, default=None,
                                  related_name="answer_answered", on_delete=models.CASCADE,
                                  help_text="direct to a specific reply, reply to a reply，null means reply the post")
