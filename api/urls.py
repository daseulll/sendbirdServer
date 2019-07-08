from django.urls import path
from . views import ChatListAPIView, ProccessHookView, MessageAPIView


urlpatterns = [
    path('', ChatListAPIView.as_view(), name='chatlist'),
    path('message/<int:id>', MessageAPIView.as_view(), name='message'),
    path('hook/', ProccessHookView.as_view(), name='hook'),
]
