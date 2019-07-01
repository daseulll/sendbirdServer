
### index page
def group_create(data):
    # 채팅방 리스트 생성 
    print(data['category'])
    # data['member'][0]['user_id']와 data['member'][1]['user_id']의 채팅방

def group_remove(data):
    # 채팅방 내에 A가 채팅방을 삭제했음을 알림
    print(data['category'])

def group_leave(data):
    # A유저가 채팅방을 나갔습니다 알림
    print(data['category'])

### detail page
def message_send(data):
    # 메세지 컨텐츠 생성
    print(data['category'])
    
def message_update(data):
    # 메세지 수정 내역 남기기
    print(data['category'])

def message_delete(data):
    # 메세지 삭제 내역 남기기
    print(data['category'])

