# import discord
# import asyncio
from han_info import han


# info = han_info.HAN();

# @brief    가장 앞의'한이', '한이야' 단어 삭제
# @details  문자열에서 가장 앞에 오는 '한이', '한이야' 단어를 삭제한다.
# @param    strign target_msg
# return    string으로 반환한다.
def delete_startswitch(target_msg):
    target_msg = target_msg.strip()
    # 문장에서 한이야 라는 단어로 시작하면 해당 단어를 제거한다.
    if target_msg.startswith("한이야"):
        target_msg = target_msg.replace("한이야", "", 1)
    # 문장에서 한이 라는 단어로 시작하면 해당 단어를 제거한다.
    elif target_msg.startswith("한이"):
        target_msg = target_msg.replace("한이", "", 1)

    # 문장의 앞과 뒤의 공백을 제거하고 반환한다.
    return target_msg.strip()


# han_process
# @brief    한이 on_message 에서의 처리를 위한 프로세스
# details   한이가 받아온 사용자의 메세지를 여기에서 전부 처리하여 반환한다.
# details   한이의 응답, 서버 정보, 정보, 도움말, 디스코드, 배우자 에 관한 기능을 처리한다.
# @param    message message
# @return   embed 또는 string으로 서버에 보낼 메세지를 반환한다.
def han_process(message):
    # 받아온 mescsage 객체에서 사용자가 입력한 문장을
    # org_msg(original_message) 변수에 저장  메시지 원본
    org_msg = message.content

    # prc_msg(process_message) 변수에 저장   처리될 메시지
    # '한이', '한이야' 단어를 제거하여 prc_msg 에 저장한다.
    prc_msg = delete_startswitch(org_msg)

    # 콘솔에 처리된 내용을 출력한다.
    print(org_msg + " / " + prc_msg)

    # 명령어에 대하여 동작하는 코드이다.
    # 명령의 결과를 문자열 또는 임베드 형태로 반환한다.
    if prc_msg.startswith("서버정보"):
        return han.server(message, str(message.author.id))

    elif prc_msg.startswith("정보"):
        return han.info()

    elif prc_msg.startswith("도움말"):
        return han.help()

    elif prc_msg.startswith("디스코드") or prc_msg.startswith("링크주소") or prc_msg.startswith("링크"):
        return han.url

    elif prc_msg.startswith("배우자") or prc_msg.startswith("배워"):
        return "배우기 기능은 아직 작성중이야"

    # None 을 반환하면 에러를 발생시키므로 예외처리 구문이 필요하다.
    return None
