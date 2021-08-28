import discord
import asyncio

# 반환형태는 무조건 임베드
def han_process(message) :
    msg = message.content
    msg = msg.replace("한이야", "")
    msg = msg.replace("한이", "")
    msg = msg.strip()
    print(msg)
    if msg[:4] == "서버정보":
        # embed = discord.Embed(title="디스코드 방 정보", description="서버의 정보들을 알려줄게!\n", color=han.color)
        embed = discord.Embed(title="디스코드 방 정보", description="서버의 정보들을 알려줄게!\n")
        embed.add_field(name="방 생성일자:", value=message.guild.created_at, inline=True)
        embed.add_field(name="멤버 수:", value=message.guild.member_count, inline=False)
        embed.add_field(name="방 부스트 단계:", value=message.guild.premium_tier, inline=False)
        embed.add_field(name="방 부스트 개수:", value=message.guild.premium_subscription_count, inline=True)
        embed.set_footer(text="발신자: " + str(message.author.id))
        # embed.set_footer(text="발신자: " + username)
        return embed
    if msg[:2] == "안녕":
        return "안녕"
    return None