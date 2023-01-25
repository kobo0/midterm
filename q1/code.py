class AIChatBot:
	def main():
		def showSubjectName():
			print("Artificial Intelligeence System for Robots")
			
		def showStudentYear():
			ID  = input()
			num = int(ID[0:2])
			sub = 66-num
			print(sub)
			
		def calculator():
			operator = input()
			x = input()
			y = input()
			if operator == '+':
				add = int(x)+int(y)
				print(add)
			if operator == '-':
				sub = int(x) - int(y)
				print(sub)
				
		while(1):
			pointer = input()
			if pointer == 'subject':
				showSubjectName()
			if pointer == 'year':
				showStudentYear()
			if pointer == 'calc':
				calculator()
			
	main()

AIChatBot()
			
