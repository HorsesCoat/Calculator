'''
Calculator v. 0.2
'''

def input_number():
	num = input("Введите число:")
	num = float(num)
	return num

def input_oper():
	oper = input("Операция('*','','+','-'):")
	return oper

def calc_me(x,y, oper):
	if oper == '*':
		return x * y
	elif oper == '/':
	   # если делитель == 0 то возвращаем ошибку
	   if y == 0:
	      return "ERROR: Divide by zero!"
	    else:
		return x / y
	elif oper == '+':
		return x + y
	elif oper == '-':
		return x-y
	else:
	  return "ERROR: Uknow operation"

def body():
  # результат работы функции input_number запишется в переменную number1
  number1 = input_number()
  # результат работы функции input_oper запишется в переменную oper
  oper = input_oper()
  # результат работы функции input_number запишется в переменную number2
  number2 = input_number()
  # вызываем функцию calc_me с переменными которые мы ранее получили
  # результат запишем в переменную result
  result = calc_me(number1,number2,oper)
  # выводим результат для пользователя
print(result)

# это специальное служебное условие Python
if__name__=='__main__':
# оно говорит, что если мы вызвали этот файл в консоли
# то надо выполнить функцию body
body()

# результат работы функции input_number запишется в переменную number1
number1 = input_number()
# результат работы функции input_oper запишется в переменную oper
oper = input_oper()
# результат работы функции input_number запишется в переменную number2
number2 = input_number()
# вызываем функцию calc_me с переменными которые мы ранее получили
# результат запишем в переменную result
result = calc_me(number1,number2,oper)
# выводим результат для пользователя
print(result)

a = "2"
b = "3.333333"
c = int(a)
print(c)
c = float(b)
print(c)