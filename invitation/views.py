from knox.auth import TokenAuthentication
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from util.pagination import MyPageNumberPagination

# the class just receive all the message that post by user
class MessageListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageListSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = MyPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user__id', 'content', ]
    ordering_fields = ['id', 'created_time']
    ordering = ('id',)

# view the message content
class MessageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = MessageCreateSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return MessageModel.objects.filter(user=self.request.user)

#view the answer content
class AnswerViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = AnswerDetailSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return AnswerModel.objects.filter(user=self.request.user)
