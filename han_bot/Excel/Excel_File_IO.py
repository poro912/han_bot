import openpyxl


class EXCEL:
	file_dir = ""
	file_name = ""
	workbooks = None
	
	def __init__(self, file_name):
		self.file_name = file_name + ".xlsx"
		self.file_dir = "./" + self.file_name
		
	def open(self):
		self.workbooks = openpyxl.load_workbook(self.file_name, data_only=True)
	
	def close(self):
		# 내용을 저장 한 후 파일 닫기
		self.workbooks.save(self.file_name)
		self.workbooks.close()


# super(QA_FILE, self).__init__()
class QA_FILE(EXCEL):
	qna_space = None
	user_space = None
	
	# 엑셀 파일에 대한 객체를 생성할 때 사용하는 메소드
	def __init__(self, file_name):
		super().__init__(file_name)
		
	# 파일을 닫았다 열여 변경사항을 적용하고 저장한다.
	def save(self):
		self.close()
		self.open()
	
	def open(self):
		super().open()
		self.qna_space = self.workbooks['QnA']
		self.user_space = self.workbooks['USER']
	
	# 파일의 내용이 정상인지 확인하는 메소드
	def integrity(self):
		pass
	
	# 질의를 등록하는 메소드
	def data_add(self, question, answer):
		pass
	
	# 리스트 형태로 답변 목록을 읽어오는 메소드
	def data_read(self, question):
		pass
	
	# 답변중에 하나를 읽어오는 메소드
	def data_rnadon_read(self, question):
		pass
	
	# 질의가 존재하는지 읽어오는 메소드
	def is_data_exist(self, question, answer):
		pass
	

class BLACK_LIST_FILE(EXCEL):
	black_space = None
	
	def __init__(self, file_name):
		super().__init__(file_name)
		
	def open(self):
		super().open()
		self.black_space = self.workbooks['Black']
		
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
QA_file = QA_FILE("QnA")
Black_list = BLACK_LIST_FILE("BlackWord")
print("엑셀 파일 열기 완료")
