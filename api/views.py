import json
from base64 import b64decode
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework import generics
from . serializers import ChatListSerializer, ChatListCreateSerializer
from . models import ChatList
from . import webhook_events


class ChatListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ChatList.objects.all()
    serializer_class = ChatListSerializer


class ProccessHookView(APIView):
    permission_classes = (AllowAny,)

    def proccess_webhook(self, data):
        event_name = data["category"]
        if event_name == 'group_channel:create':
            webhook_events.group_create(data)
        if event_name == 'group_channel:remove':
            webhook_events.group_remove(data)
        if event_name == 'group_channel:leave':
            webhook_events.group_leave(data)
        if event_name == 'group_channel:message_send':
            webhook_events.message_send(data)
        if event_name == 'group_channel:message_update':
            webhook_events.message_update(data)
        if event_name == 'group_channel:message_delete':
            webhook_events.message_delete(data)


    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        self.proccess_webhook(data)
        print("json.loads : {}".format(data))
        return Response(status=status.HTTP_200_OK)
