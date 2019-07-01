from django.urls import path
from . views import ChatListAPIView, ProccessHookView


urlpatterns = [
    path('', ChatListAPIView.as_view(), name='chatlist'),
    path('hook/', ProccessHookView.as_view(), name='hook')
]