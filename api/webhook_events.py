from . models import User, ChatRoom, Message

def init(data):
    user1 = User.objects.get_or_create(email=data['members'][0]['user_id'], nickname=data['members'][0]['nickname'])
    user1 = User.objects.get(email=data['members'][0]['user_id'], nickname=data['members'][0]['nickname'])

    user2 = User.objects.get_or_create(email=data['members'][1]['user_id'], nickname=data['members'][1]['nickname'])
    user2 = User.objects.get(email=data['members'][1]['user_id'], nickname=data['members'][1]['nickname'])

    chatroom = ChatRoom.objects.filter(channel_url=data['channel']['channel_url'])
    if chatroom:
        return False
    else:
        ChatRoom.objects.get_or_create(
            user1=user1, user2=user2, 
            channel_url=data['channel']['channel_url'], 
            roomname=data['channel']['name']
        )
        return True

def group_create(data):
    # 채팅방 리스트 생성 
    init(data)

def group_remove(data):
    # 채팅방 내에 A가 채팅방을 삭제했음을 알림
    print(data['category'])

def group_leave(data):
    # A유저가 채팅방을 나갔습니다 알림
    print(data['category'])

def message_send(data):
    # 메세지 컨텐츠 생성
    init(data)
    sender = User.objects.get(email=data['sender']['user_id'])
    channel = ChatRoom.objects.get(channel_url=data['channel']['channel_url'])
    message = data['payload']['message']
    message_id = data['payload']['message_id']
    Message.objects.create(sender=sender, channel=channel, message=message, message_id=message_id)

    
def message_update(data):
    # 메세지 수정 내역 남기기
    print(data['category'])

def message_delete(data):
    # 메세지 삭제 내역 남기기
    print(data['category'])

