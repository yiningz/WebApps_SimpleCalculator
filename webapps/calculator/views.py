from django.shortcuts import render

def calculate(request):
		result = dict()
		display = 'display'
		num1 = 'num1'
		op = 'op'
		num2 = 'num2'
		error = 'error'
		count = ifCal(request)

		if(request.method == "GET"):
			if('num' in request.GET):
				num = request.GET['num']
				# input is a digital number
				if(count == 0):
					result[num1] = num
				elif(count == 1):
					result[num1] = str(int(num) + int(request.GET['num1'])*10)
				elif(count == 2):
					result[num2] = num
					result[num1] = request.GET['num1']
					result[op] = request.GET['op']		
				else:
					result[num1] = request.GET['num1']
					result[op] = request.GET['op']
					result[num2] = str(int(request.GET['num2']) * 10 + int(num))
				return render(request, 'Login.html', result)
			elif('operator' in request.GET):
				if(count == 0):
					pass
				elif(count == 1 or count == 2):
					result[num1] = request.GET['num1']
					result[op] = request.GET['operator']
				elif(count == 3):
					preOp =request.GET['op']
					number1 = request.GET['num1']
					number2 = request.GET['num2']
					if(number2 == "0" and preOp == u"\u00F7"):
						result[error] = "ERROR"
					else:
						if(preOp == "+"):
							result[num1] = str(int(number1) + int(number2))
						elif(preOp == "-"):
							result[num1] = str(int(number1) - int(number2))
						elif(preOp == u"\u00F7"):
							result[num1] = str(int(int(number1) / int(number2)))
						else:
							result[num1] = str(int(number1) * int(number2))
						result[op] = request.GET['operator']						
				return render(request, 'Login.html', result)
			else:
				if(count <= 2):
					pass
				else:
					preOp = request.GET['op']
					num1 = request.GET['num1']
					num2 = request.GET['num2']
					if(num2 == "0" and preOp == u"\u00F7"):
						result[error] = "ERROR"
					else:
						if(preOp == '+'):
							result[display] = str(int(num1) + int(num2))
						elif(preOp == '-'):
							result[display] = str(int(num1) - int(num2))
						elif(preOp == u"\u00F7"):
							result[display] = str(int(int(num1) / int(num2)))
						else:
							result[display] = str(int(num1) * int(num2))			
				return render(request, 'Login.html',result)




def ifCal(request):
		count = 0
		if('num1' in request.GET and request.GET['num1'] != ''):
			count += 1
		if('op' in request.GET and request.GET['op'] !=''):
			count += 1
		if('num2' in request.GET and request.GET['num2'] != ''):
			count += 1
		return count



