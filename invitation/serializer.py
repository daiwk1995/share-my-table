from rest_framework import serializers as srs

from .models import *
from user.serializer import UserIntroSerializer

#rewrite the answer format
class AnswerSerializer(srs.ModelSerializer):
    user = UserIntroSerializer()
    created_time = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AnswerModel
        fields = ['id', 'user', 'content', 'created_time']

#rewrite the reply to answer format
class SubAnswerSerializer(srs.ModelSerializer):
    user = UserIntroSerializer()
    answer_to = AnswerSerializer()
    created_time = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AnswerModel
        fields = ['id', 'user', 'content', 'created_time', 'answer_to']

#rewrite the message list format
class MessageListSerializer(srs.ModelSerializer):
    created_time = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    user = UserIntroSerializer()
    message_answered = SubAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = MessageModel
        fields = ['id', 'user', 'content', 'created_time', 'message_answered']

#rewrite the message create format
class MessageCreateSerializer(srs.ModelSerializer):
    user = srs.HiddenField(
        default=srs.CurrentUserDefault(), write_only=True
    )
    created_time = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = MessageModel
        fields = ['user', 'content', 'created_time']

#rewrite the whole answer format
class AnswerDetailSerializer(srs.ModelSerializer):
    user = srs.HiddenField(
        default=srs.CurrentUserDefault()
    )
    created_time = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    answer_to = srs.PrimaryKeyRelatedField(required=False, queryset=AnswerModel.objects.all(),
                                           help_text="reply to a reply")

    class Meta:
        model = AnswerModel
        fields = '__all__'
