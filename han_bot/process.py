import discord
import asyncio
import han_info

info = han_info.HAN();


# 반환형태는 무조건 임베드
def han_process(message):
    msg = message.content
    msg = msg.replace("한이야", "")
    msg = msg.replace("한이", "")
    msg = msg.strip()
    print(msg)

    if msg[:4] == "서버정보":
        return info.server(message, str(message.author.id))
    if msg[:2] == "정보":
        return info.info()
    if msg[:3] == "도움말":
        return info.help()
    if msg[:2] == "서버" or msg[:4] == "서버":
        return info.han.url

    return None
