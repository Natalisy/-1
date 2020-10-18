# Задание 1
 #phrase_1 = input()
 #phrase_2 = input()

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if phrase_1 < phrase_2:
	print("Фраза 1 длиннее фразы 2")
elif phrase_2 < phrase_1:
	print("Фраза 2 длиннее фразы 1")
else:
	print("Фразы равной длины")


#Задание 2

#year = int(input())

year = int(input())

year_str = str(year)

last_two_numbers = year_str[:-3:-1]

if last_two_numbers == "00":
	if year%400 == 0:
		print("Високосный год")

elif year%4 == 0:
	print("Високосный год")

else:
	print("Обычный год")


#Задание 3

### 21 марта – 20 апреля Овен

'''21 апреля – 21 мая Телец

22 мая – 21 июня Близнецы

22 июня – 22 июля Рак

23 июля – 23 августа Лев

24 августа – 22 сентября Дева

23 сентября – 22 октября Весы

23 октября – 22 ноября Скорпион

23 ноября – 21 декабря Стрелец

22 декабря – 20 января Козерог

21 января – 19 февраля Водолей

20 февраля – 20 марта Рыбы '''

# znaki = ['Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']

print("Введите день")
day = int(input())

print("Введите месяц")
month_of_birth = input().lower()

number_of_month = 0
count = 0

months = ['декабрь', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь']


for month in months:
	if month == month_of_birth:
		number_of_month = count
		break
	else:
		count+=1

if number_of_month == 0: #декабрь
	if day >= 22:
		print("Козерог")
	else:
		print("Стрелец")

if number_of_month == 1: # январь
	if day >= 21:
		print("Водолей")
	else:
		print("Козерог")

if number_of_month == 2: # февраль
	if day >= 20:
		print("Рыбы")
	else:
		print("Водолей")

if number_of_month == 3: # март
	if day >= 21:
		print("Овен")
	else:
		print("Рыбы")

if number_of_month == 4: # апрель
	if day >= 21:
		print("Телец")
	else:
		print("Овен")


# Задание 4

print("Введите размеры посылки в сантиметрах")

print("Введите ширину")
width = int(input())

print("Введите длину")
length = int(input())

print("Введите высоту")
height = int(input())

if width < 15 and length < 15 and height < 15:
	print("Коробка №1")

elif 15<= width <50 or  15<= length <50 or 15<= height <50:
	print("Коробка №2")

elif length >= 200:
	print("Упаковка для лыж")

else:
	print("Стандартная коробка №3")


