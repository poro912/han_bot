class FILE:
	file_dir = ""
	file_name = ""
	fp = None
	
	def __init__(self):
		file_dir = ""
		fp = None
	
	def file_open(self):
		pass
	
	def file_close(self):
		pass


class QA_FILE(FILE):
	# 파일의 내용이 정상인지 확인하는 메소드
	def integrity(self):
		pass
	
	# 질의를 등록하는 메소드
	def data_add(self, Question, Answer):
		pass
	
	# 리스트 형태로 답변 목록을 읽어오는 메소드
	def data_read(self, Question):
		pass
	
	# 답변중에 하나를 읽어오는 메소드
	def data_rnadon_read(self, Question):
		pass
	
	# 질의가 존재하는지 읽어오는 메소드
	def is_data_exist(self, Question, Answer):
		pass


class BLACK_LIST_FILE(FILE):
	# 무결성을 확인하는 메소드
	def integrity(self):
		pass
	
	# 블랙리스트 목록을 읽어오는 메소드
	def data_read(self):
		pass
	
	# 블랙리스트에 문장을 추가하는 메소드
	def data_add(self, string):
		pass
	
	# 블랙리스트에 문자열이 포함되어 있는지 확인하는 메소드
	def is_incldue(self, string):
		pass


# 파일을 연다.
QA_file = QA_FILE()
QA_file.file_open()
Black_list = BLACK_LIST_FILE()
Black_list.file_open()