import json
from base64 import b64decode
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework import generics
from . models import ChatRoom, Message
from . serializers import ChatListSerializer, MessageSerializer
from . import webhook_events


class ProccessHookView(APIView):
    permission_classes = (AllowAny,)

    def proccess_webhook(self, data):
        event_name = data["category"]
        if event_name == 'group_channel:create':
            webhook_events.group_create(data)
        # if event_name == 'group_channel:remove':
        #     webhook_events.group_remove(data)
        # if event_name == 'group_channel:leave':
        #     webhook_events.group_leave(data)
        if event_name == 'group_channel:message_send':
            webhook_events.message_send(data)
        # if event_name == 'group_channel:message_update':
        #     webhook_events.message_update(data)
        # if event_name == 'group_channel:message_delete':
        #     webhook_events.message_delete(data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        self.proccess_webhook(data)
        # print("json.loads : {}".format(data))
        return Response(status=status.HTTP_200_OK)


class ChatListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        serializer = ChatListSerializer(ChatRoom.objects.filter(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MessageAPIView(APIView):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        channel_id = self.kwargs.get("id", None)
        return Message.objects.filter(channel__id=channel_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
