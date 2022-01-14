import discord


class HAN:
    # 한이의 대표 서버의 url
    url = "https://discord.gg/YKnrnffqEP"

    # 한이의 대표 이미지 url
    image = "https://cdn.discordapp.com/attachments/810130135437017088/810374859028824096/123_20210214135940.png"

    # 한이의 퍼스널 컬러
    color = 0x70ABE1

    # 현재 버전
    version = "beta 1.0"

    # 출력용 구분선
    _line = "**--------------------------------------**"

    # @brief    한이의 개발 정보를 임베드 형태로 반환
    # @details  한이의 사진, 각 처부별 담당자, 제작 날짜,
    # @details  제작정보, 사용 언어, 상세 정보, 봇 이름, 봇 버전
    # @details  등의 세부 내용을 임베드 형태로 반환한다.
    # @return   embed
    def info(self):

        embed = discord.Embed(title="한이 프로필", description="내 정보들을 알려줄게!\n", color=self.color)
        embed.add_field(name="개발자", value=self._line, inline=False)
        embed.add_field(name="코딩", value="**포로(주, 최적화)**\n**에브(보조, 아이디어)**", inline=True)
        embed.add_field(name="일러스트", value="**사과머리(현 서버 아이콘, 봇 프로필)**\n설하(서버 아이콘)\n베루니아(봇 프로필)", inline=True)
        embed.add_field(name="도움", value="! ReadyTxT(몇몇 기능, 웹사이트)", inline=False)
        embed.add_field(name="제작일", value="2021년 1월 14일", inline=True)
        embed.add_field(name="제작 정보", value=self._line, inline=False)
        embed.add_field(name="사용 언어", value="Python 3.8", inline=True)
        embed.add_field(name="상세 정보", value=self._line, inline=False)
        embed.add_field(name="봇 이름", value="한(HAN)", inline=True)
        embed.add_field(name="봇 버전", value=self.version, inline=True)
        embed.set_footer(text="한이 봇의 저작권은 개발진에게 있음을 알립니다.")
        embed.set_thumbnail(url=self.image)
        return embed

    # @brief    현재 서버의 정보를 임베드 형태로 반환
    # @details  현재 한이가 속해있는 서버의 정보
    # @details  서버 이름, 방 정보, 멤버의 수 등을 임베드 형태로 반환한다.
    # @return   embed
    def server(self, message, username):

        embed = discord.Embed(title="디스코드 방 정보", description="서버의 정보들을 알려줄게!\n", color=self.color)
        embed.add_field(name="방 생성일자:", value=message.guild.created_at, inline=True)
        embed.add_field(name="멤버 수:", value=message.guild.member_count, inline=False)
        embed.add_field(name="방 부스트 단계:", value=message.guild.premium_tier, inline=False)
        embed.add_field(name="방 부스트 개수:", value=message.guild.premium_subscription_count, inline=True)
        embed.set_footer(text="발신자: " + username)
        return embed

    # @brief    한이의 명령어 목록을 임베드 형태로 반환
    # @details  한이 사용시에 쓸 수 있는 명령어들의 목록을 임베드 형태로 반환한다.
    # @return   embed
    def help(self):

        embed = discord.Embed(title="명령어 목록", description="나랑 대화 하고 놀려면 명령어 정도는 알아야겠지~? \n여기 도움말이야!", color=self.color)
        embed.add_field(name="- 한이야 [A]",
                        value="**``한이야 [A]``**는 나랑 소통하기 위한 기본 **접두사**!\n" +
                              "접두사가 뭐냐고? 음... 마인크래프트로 따지면 명령어 실행할때 쓰는 **``/``**와 같아!\n\n" +
                              "[ 사용 예시 : ``한이야 안녕`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 배우자 [A] / [B]",
                        value="**``한이야 배우자 [A] / [B]``**는 나에게 단어를 가르쳐줄 수 있는 멍령어야! \n이걸로 저에게 단어를 가르칠 수 있어! \n" +
                              "(나한태 이상한거 가르치면 죽어 ㅡ3ㅡ)\n\n" +
                              "[ 사용 예시 : ``한이야 배우자 냉면 / 맛있어!!!`` ] \n" +
                              "``유저 : 냉면, 한이 : 맛있어!!!.`` \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 링크 & 디스코드",
                        value="**``한이야 링크 & 디스코드``**는 내가 만들어지는 커뮤니티로 들어갈 수 있는 링크를 주는 명령어야!\n\n" +
                              "[ 사용 예시 : ``한이야 링크`` 혹은 ``한이야 디스코드`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 서버정보",
                        value="**``한이야 서버정보``**는 해당 서버의 정보를 보여주는 명령어이야!\n" +
                              "방 생성일자, 멤버 수, 방 소유자 등등 많은 정보들을 볼 수 있어!\n\n" +
                              "[ 사용 예시 : ``한이야 서버정보`` ] \n" + self._line, inline=False)

        embed.add_field(name="- 한이야 정보",
                        value="**``한이야 정보``**는 내 정보를 알려주는 명렁어야!\n" +
                              "아빠(제작자)랑, 생일(제작년도), 출생지(사용 언어) 등등 많은 정보들을 볼 수 있어!(근대 별로 쓸모는 없엉😋)\n\n" +
                              "[ 사용 예시 : ``한이야 정보`` ]\n" + self._line, inline=False)
        embed.set_thumbnail(url=self.image)
        return embed

    # @brief    배우자 명령어 실패 시 출력할 임베드 형태
    # @details  배우자 명령어가 실패한 경우에 예시를 보여주기위해 해당 임베드를 반환한다.
    # @return   embed
    def learn_error_msg(self):

        embed = discord.Embed(title="잘못된 형식이야!", description="그렇게로는 날 가르칠 수 없어!", color=self.color)
        embed.add_field(name="사용법", value="""
        **한이야 배우자 [배울 말] / [답변할 말]**
        이렇게 입력해야돼!

        **[ 예시 ]**
        한이야 배우자 냉면 / 맛있어!!!
        User: 한이야 냉면
        한이: 맛있어!!!""", inline=False)
        embed.set_thumbnail(url=self.image)
        return embed


han = HAN()
