akk = input("Введите имя аккаунта:")
if akk == "kostya":
	pas = input("введи пароль:")
elif akk != "kostya":
	print("такого логина нет")
if pas == "123":
		print("Добро пожаловать Константин")
		s = input("вы хотите открыть калькулятор? ")
		if s == "да":
			print("вы открыли калькулятор")
			a = int (input("введи первое число: "))
			b = int (input("введи второе число: "))
			w = a + b
			print ("результат:", (w) )
		elif s == "нет":
			print("идет закрытие програмы калькулятор")
else:
	print("логин или пароль были введены не верно")
