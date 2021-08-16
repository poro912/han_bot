#git hub test
import os
import sys
import discord
import asyncio

#파일 시스템 구축
files = ["Excl", "Option", "Admin", "Token"]
path = os.path.dirname(os.path.realpath(__file__))
path.replace("\\","/")
#파일 시스템 등록
for i in files:
    sys.path.append(path+"\\"+i)
    print(path+"\\"+i)

#파일 시스템 임포트
#from Excl import *
#from Option import *
#from Admin import *
from Token import *


global msg;

token_type = "origin"
client = discord.Client()

@client.event
async def on_ready():
    print(os.path.dirname(os.path.realpath(__file__))+"\\Excl")
    print("**--------------------------------------**")
    print(client.user.id)
    #print("버전" + han.ver)
    #print("이름 : " + client.user.name)
    print("**--------------------------------------**")
    await client.change_presence(status=discord.Status.online , activity=discord.Game("'한이야 도움말' 입력! / 제작 이음, 포로"))

@client.event
async def on_message(message):
    msg = message
    if message.content.startswith("한이") :
        ''' 한이 주요 코드부'''
        # await message.channel.send("우씨... 나 말 안해!😡");
        #message_submit(message);
        print("실행")
        print(" : ",__build_class__)
        print("파일 위치 : ",__file__)

Token.set_token()
global test_token
client.run(Token.ret_token(token_type))



# @client.event
"""
try:

except:
"""

# token.get_token();


