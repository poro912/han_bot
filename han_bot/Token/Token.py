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


class Tokens:
	def __init__(self):
		self.test = None
		self.main = None

	# ../../code.txt 파일로부터 토큰을 읽어와 토큰을 저장한다.
	# 위에서부터 테스트토큰, 메인토큰 순으로 저장된다.
	def set(self):
		file_name = "code.txt"

		before = os.getcwd()
		os.chdir("../../")
		now = os.getcwd()
		file = open(now + "/" + file_name, "r")

		self.test = file.readline()
		self.main = file.readline()

		print("토큰 가져오기 완료")
		os.chdir(before)
		return

	# 토큰을 반환 한다.
	def get(self, type):
		if type == 1 or type == "origin" or type == "1":
			return self.main
		if type == 2 or type == "test" or type == "2":
			return self.test