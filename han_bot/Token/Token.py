import os

def set_token():
    global han_token
    global test_token
    file_name = "code.txt"

    before = os.getcwd()
    os.chdir("../../")
    now = os.getcwd()
    file = open(now + "/" + file_name, "r")

    test_token = file.readline()
    han_token = file.readline()

    print("토큰 가져오기 완료")
    os.chdir(before)


def ret_token(type):
    global test_token
    global han_token
    if type == 1 or type == "origin" or type == "1":
        return test_token
    if (type == 2 or type == "test" or type == "2"):
        return han_token
