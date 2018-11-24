from rest_framework.routers import DefaultRouter

from invitation.views import *

router = DefaultRouter()

router.register(r'messages', MessageListViewSet, base_name='messages')
router.register(r'message', MessageViewSet, base_name='message')
router.register(r'answer', AnswerViewSet, base_name='answer')

urlpatterns = [
    *router.urls,
]
