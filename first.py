def divide_number(num1, num2):
   try:
		return (num1/num2)
	except ZeroDivisionError:
		print("Cannot Divide by zero")
