import discord


class HAN:
    # 서버 url
    # 이미지 url
    # 퍼스널 컬러
    # 버전
    url = "https://discord.gg/6NdvzzPRAU"
    image = "https://media.discordapp.net/attachments/869887087959216168/881478475410718721/68.png?width=676&height=676"
    color = 0x70ABE1
    version = "beta 1.0"

    _line = "**--------------------------------------**"

    def __init__(self):
        pass

    def info(self):
        # 한이 개발 정보를 임베드 형태로 변환
        embed = discord.Embed(title="한이 프로필", description="내 정보들을 알려줄게!\n", color=self.color)
        embed.add_field(name="개발자", value=self._line, inline=False)
        embed.add_field(name="코딩", value="**포로(주, 최적화)**\n**빼액(보조, 아이디어)**", inline=True)
        embed.add_field(name="일러스트", value="**사과머리(현 서버 아이콘, 봇 프로필)**\n설하(서버 아이콘)\n베루니아(봇 프로필)", inline=True)
        embed.add_field(name="도움", value="! ReadyTxT(몇몇 기능, 웹사이트)", inline=False)
        embed.add_field(name="제작일", value="2021년 1월 14일", inline=True)
        embed.add_field(name="제작 정보", value=self._line, inline=False)
        embed.add_field(name="사용 언어", value="Python 3.8", inline=True)
        embed.add_field(name="상세 정보", value=self._line, inline=False)
        embed.add_field(name="봇 이름", value="한(HAN)", inline=True)
        embed.add_field(name="봇 버전", value=self.version, inline=True)
        embed.set_footer(text="한이 봇의 저작권은 Han 개발진에게 있음을 알립니다.")
        embed.set_thumbnail(url=self.image)
        return embed

    def server(self, message, username):
        # 서버정보를 임베드 형태로 반환
        embed = discord.Embed(title="디스코드 방 정보", description="서버의 정보들을 알려줄게!\n", color=self.color)
        embed.add_field(name="방 생성일자:", value=message.guild.created_at, inline=True)
        embed.add_field(name="멤버 수:", value=message.guild.member_count, inline=False)
        embed.add_field(name="방 부스트 단계:", value=message.guild.premium_tier, inline=False)
        embed.add_field(name="방 부스트 개수:", value=message.guild.premium_subscription_count, inline=True)
        embed.set_footer(text="발신자: " + username)
        return embed

    def help(self):
        # 한이의 명령 목록을 임베드 형태로 반환
        embed = discord.Embed(title="명령어 목록", description="나랑 대화 하고 놀려면 명령어 정도는 알아야겠지~? \n여기 도움말이야!", color=self.color)
        embed.add_field(name="- 한이야 [A]",
                        value="**``한이야 [A]``**는 나랑 소통하기 위한 기본 **접두사**!\n"
                              + "접두사가 뭐냐고? 음... 마인크래프트로 따지면 명령어 실행할때 쓰는 **``/``**와 같아!\n\n"
                              + "[ 사용 예시 : ``한이야 안녕`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 배우자 [A] / [B]",
                        value="**``한이야 배우자 [A] / [B]``**는 나에게 단어를 가르쳐줄 수 있는 멍령어야! \n이걸로 저에게 단어를 가르칠 수 있어! \n"
                              + "(나한태 이상한거 가르치면 죽어 ㅡ3ㅡ)\n\n"
                              + "[ 사용 예시 : ``한이야 배우자 유냉면 / 맛 업성...`` ] \n"
                              + "``유저 : 유냉면, 한이 : 맛 업성...`` \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 링크 & 디스코드",
                        value="**``한이야 링크 & 디스코드``**는 내가 만들어지는 커뮤니티로 들어갈 수 있는 링크를 주는 명령어야!\n\n"
                              + "[ 사용 예시 : ``한이야 링크`` 혹은 ``한이야 디스코드`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 서버정보",
                        value="**``한이야 서버정보``**는 해당 서버의 정보를 보여주는 명령어이야!\n"
                              + "방 생성일자, 멤버 수, 방 소유자 등등 많은 정보들을 볼 수 있어!\n\n"
                              + "[ 사용 예시 : ``한이야 서버정보`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 정보",
                        value="**``한이야 정보``**는 내 정보를 알려주는 명렁어야!\n"
                              + "아빠(제작자)랑, 생일(제작년도), 출생지(사용 언어) 등등 많은 정보들을 볼 수 있어!(근대 별로 쓸모는 없엉😋)\n\n"
                              + "[ 사용 예시 : ``한이야 정보`` ]\n" + self._line, inline=False)
        embed.set_thumbnail(url=self.image)
        return embed

    def learn_error_msg(self):
        embed = discord.Embed(title="잘못된 형식이야!", description="그렇게로는 날 가르칠 수 없어!", color=self.color)
        embed.add_field(name="사용법", value="""
        **한이야 배우자 [배울 말] / [답변할 말]**
        이렇게 입력해야되!

        **[ 예시 ]**
        한이야 배우자 유냉면 / 맛 없어...
        User: 한이야 유냉면
        Bot: 맛 없어...""", inline=False)
        embed.set_thumbnail(url=self.image)
        return embed
