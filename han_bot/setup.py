# -*- coding: utf-8 -*-
# 한이 프로젝트 디스코드 챗봇 프로젝트의 메인 파일이다.
# 해당 파일에서는 한이의 파일시스템 구축 및 스크립팅에 대한 코드가 작성되어있다.


import os
import sys
import process
# pip install discord
import discord

# import asyncio
# import han_info

# 파일 시스템 구축
# 파일을 현재 프로젝트에 포함시키기위한 코드이다.
# 파일 이름들을 등록
files = ["Excl", "Option", "Admin", "Token", "Emoji"]

# 현재 파일의 주소를 가져옴
path = os.path.dirname(os.path.realpath(__file__))

# 문자열 변환 작업을 통하여 로컬 주소로 변경
path.replace("\\", "/")

# files에 있는 디렉터리를 파일 시스템에 등록
for i in files:
	sys.path.append(path + "\\" + i)
	print(path + "\\" + i)


# 파일 시스템 임포트
# from Excl import *
# from Option import *
# from Admin import *
from Token import Token


# 여기에 토큰 타입을 명시하면 해당하는 토큰을 가져옴 "origin" "test"
token_type = "test"
client = discord.Client()


# 클라이언트가 준비되면 버전을 출력한다.
@client.event
async def on_ready():
	print(os.path.dirname(os.path.realpath(__file__)) + "\\Excl")
	print("**--------------------------------------**")
	print(client.user.id)
	# print("버전" + han.ver)
	# print("이름 : " + client.user.name)
	print("**--------------------------------------**")
	await client.change_presence(status=discord.Status.online, activity=discord.Game("'한이야 도움말' 입력! / 제작 이음, 포로"))


# 디스코드 상에 메세지가 입력되면 해당 부분을 실행한다.
@client.event
async def on_message(message):
	# 만약 문장의 시작에 "한이"라는 단어가 있을 경우
	# 한이 명령으로 판단하여 처리를 시작한다.
	# 한이의 주요 처리부 이다.
	if message.content.startswith("한이"):

		# message 객체를 갖고 process로 이동하여 처리한다.
		# 이 때 처리가 가능한 문장이였다면 문자열 또는 임베드 형식으로 반환받는다.
		retmsg = process.han_process(message)

		# 문자열 처리 예외처리 구문
		try:
			# 반환 형식이 임베드라면 임베드 형식으로 출력한다.
			if type(retmsg) == discord.embeds.Embed:
				await message.channel.send(embed=retmsg)

			# 반환 형식이 문자열이라면 그냥 출력한다.
			else:
				await message.channel.send(retmsg)

		# 아무것도 반환받지 못한 경우 또는 에러가 발생한 경우
		# 예외처리 구문으로 넘어가며 없는 명령이라는 문자열을 출력한다.
		except Exception:
			await message.channel.send("그건 없는 명령이야")

		# 분기를 종료한다.
		return

	# 같이 놀사람 문자로 시작한 경우
	elif message.content.startswith("같이 놀사람"):
		await message.channel.send("난 대화만 할랭😜")
		return

	elif message.content.startswith("admin"):
		pass

'''
Token.set_token()
global test_token
client.run(Token.ret_token(token_type))
'''

# 토큰을 세팅 및 토큰을 사용하여 봇에 접속
myToken = Token.Tokens()
myToken.set()
client.run(myToken.get(token_type))


# await message.channel.send("우씨... 나 말 안해!😡");
# message_submit(message);
# print("실행")
# print(" : ",__build_class__)
# print("파일 위치 : ",__file__)
