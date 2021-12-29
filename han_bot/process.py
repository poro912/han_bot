import discord
import asyncio
import han_info

info = han_info.HAN();


# 반환형태는 무조건 임베드
def han_process(message):

    # 받아온 message 객체에서 문장정보를 뽑아온다.
    # 뽑은 문장 정보에서 "한이야" 및 "한이" 단어를 앞에서부터 하나 지운다.
    msg_orgin = message.content
    msg = message.content
    msg = msg.replace("한이야", "", 1)

    # 만약 문자열의 길이 변화가 없었다면 "한이야" 라는 단어가 없는 것 으로 "한이" 단어를 지운다.
    if len(msg_orgin) == len(msg):
        msg = msg.replace("한이", "", 1)

    # 처리한 문자열의 처음과 끝에 있는 공백을 제거한다.
    msg = msg.strip()

    # 콘솔에 처리된 내용을 출력한다.
    print(message.content +" / "+ msg)

    # 처리에 따라 임베드 객체 또는 문자열을 반환한다.
    if msg[:4] == "서버정보":
        return info.server(message, str(message.author.id))
    elif msg[:2] == "정보":
        return info.info()
    elif msg[:3] == "도움말":
        return info.help()
    elif msg[:4] == "디스코드" or msg[:4] == "링크주소":
        return info.url
    elif msg[:3] == "배우자":
        return "배우기 기능은 아직 작성중이야"
        pass
    else:
        pass
    return None
