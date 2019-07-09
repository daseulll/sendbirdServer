from django.urls import path, re_path
from . views import ChatListAPIView, ProccessHookView, MessageAPIView
from chat.views import index

urlpatterns = [
    path('chat/', ChatListAPIView.as_view(), name='chatlistAll'),
    path('chat/<str:param>', ChatListAPIView.as_view(), name='chatlist'),
    path('chat/message/<int:id>', MessageAPIView.as_view(), name='message'),
    path('chat/hook/', ProccessHookView.as_view(), name='hook'),
    re_path(r'.*', index)
]
