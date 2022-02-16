print('Задача 1. Пропавшая переменная')

# Что нужно сделать
# Найдите в программе необъявленную переменную и объявите её, присвоив ей значение ‘Кот’.
pet = 'Кот'
client = 'Петя'
print(client)
print(' и ')
print(pet)
===================================================================================================
print('Задача 2. Цвета')

# Что нужно сделать
# Исправьте программу так, чтобы в результате её выполнения
# на экран в одну строку выводился текст: Red Blue Green RedGreenBlue Blue GreenBlue.
r = 'Red'
g = 'Green'
b =  'Blue'
print(r, b, g, r+g+b, b, g+b)
===================================================================================================
print('Задача 3. Животные')

# Что нужно сделать
# Создайте две переменные с именами «Первое животное» и «Второе животное» на английском языке.
# Запишите в первую переменную слово «Заяц», а во вторую — «Черепаха».
# Используя эти переменные, выведите на экран текст «Заяц спит, Черепаха идёт» в одну строку.
rabbit = 'Заяц'
turtle = 'Черепаха'
print(rabbit, 'спит,', turtle, 'идёт')
===================================================================================================
print('Задача 4. Информация о пользователе')

# Что нужно сделать
# Напишите программу, которая запрашивает некоторые данные у пользователя,
# затем выведите их на экран, как показано ниже.
# Данные должны лежать в разных переменных.
#
# Вариант 1. Запросите имя и фамилию и выведите их на экран построчно.
# Результат должен быть таким (с вашим именем и фамилией, конечно):
# Пример первого варианта:

# Введите имя: Роман
# Введите фамилию: Булгаков
# Вас зовут
# Роман
# Булгаков

# Вариант 2. Запросите имя, фамилию и город проживания,
# затем выведите их на экран в две строки: первая — «Вас зовут» и далее имя и фамилия,
# вторая — «Вы живёте в городе» и далее город.
# Для красоты отделите в консоли ввод и вывод данных, как в примере:
# Пример второго варианта:

# Введите имя: Роман
# Введите фамилию: Булгаков
# Введите город проживания: Москва
# ==========
# Вас зовут: Роман Булгаков
# Вы живете в городе Москва

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
reside = input('Введите город проживания: ')
print('Вас зовут', first_name, last_name)
print('Вы живете в городе', reside)
===================================================================================================
print('Задача 5. Вход в систему')

# Что нужно сделать
# Исправьте программу и допишите необходимые команды для получения нужного результата.
# Будьте внимательны при исправлении и помните о правилах названия переменных.

# Программа:

first_name = input('Введите имя пользователя: ')
greeting = 'Утро доброе'
print(greeting, first_name)
intro = "К сожалению, у Вас нет доступа к системе."
info = "Пожалуйста, обратитесь к системному администратору."
print(intro)
print(info)

# Ожидаемый результат:

# Введите имя пользователя: Роман
# Привет, Роман
# К сожалению, у Вас нет доступа к системе.
# Пожалуйста, обратитесь к системному администратору.
===================================================================================================
print('Задача 6. Полёт')

# Что нужно сделать
# Напишите программу для сервиса заказа билетов,
# которая запрашивает у пользователя город вылета и город прилёта.
# Затем выведите их в одну строку через тире.
# Обратите внимание на свои переменные: названия должны отражать содержимое.
print('Благодарим за выбор нашей авиакомпании!')
first_city = input('Город отправления:')
second_city = input('Город прибытия:')
print(first_city, '-', second_city)
print('Желаем приятного полёта')
===================================================================================================
print('Задача 7. Путь к файлу')

# Что нужно сделать
# К каждому файлу на компьютере можно узнать путь. Выглядит он примерно так:
# 'C:/user/docs/folder/file_name.txt'

# Напишите программу,
# которая запрашивает у пользователя его имя и имя файла (переменные user и file_name соответственно).
# Используя операцию конкатенации, выведете путь к файлу на экран.
# Пример результата:

# Введите ваше имя: Sasha
# Введите имя файла: text
# C:/user/Sasha/docs/folder/text.txt
user_name = input('Введите ваше имя:')
file_name = input('Введите название файла:')
print('C:/user/'+user_name+'/docs/folder/'+file_name+'.txt')
===================================================================================================
print('Задача 8. Обмен значений двух переменных')

# Что нужно сделать
# Дана программа, которая запрашивает у пользователя два слова, а затем выводит их на экран два раза.

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a,b)
a,b = b,a
print(a,b)


# Задача: поменять значения переменных a и b местами.
# Изменять, удалять, менять местами 6-ю, 7-ю, 8-ю и последнюю строчки нельзя.
# Но в 9-ю строку можно вставлять сколько угодно кода, не трогая последний принт.
# Пример результата работы программы:

# Введите первое слово: Сок
# Введите второе слово: Вода
# Сок Вода
# Вода Сок
===================================================================================================
print('Задача 1. Язык математики')

# Маше для защиты курсовой работы нужно написать программу для расчёта экономической модели по формуле.
# Как записать саму формулу в программу, она не знает, у неё есть только начальные значения.
# Поэтому Маша решила просто заплатить Егору, чтобы тот написал её быстрее.
#
# Дана программа:
# a = 8
# b = 10
# c = 12
# d = 18
#
# Продолжите программу:
# переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.
#
# Выражение:

# (-3 + а**2) * b - 2**3
#      c- 2 * d

a = 8
b = 10
c = 12
d = 18
result = ((-3 + (a ** 2)) * b - (2 ** 3)) / (c - (2 * d))
print(result)
===================================================================================================
print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям.
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода. И так за каждый год.
#
# Надя решила,
# что быстрее будет написать простую программу, которая сделает всё за неё.
#
#
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
numbers_1_and_2 = number1 + number2
numbers_3_and_4 = number3 + number4
result = numbers_1_and_2 / numbers_3_and_4
print(result)
===================================================================================================
print('Задача 3. Следующее и предыдущее')

# В олимпиаде по программированию участвовали 1000 человек,
# и программа автоматически распределила их по количеству баллов.
# Иногда количество баллов у участников одинаковое,
# и тогда комиссии нужно посмотреть фамилии одного из таких участников,
# а также его соседей, это реализует специальная часть алгоритма.
#
# Напишите программу,
# которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее число.
# Результат:

# Введите число: 5
# После числа 5 идет число 6
# До числа 5 идет число 4
number = int(input('Введите число: '))
previous_number = number - 1
print('До числа', number, 'идет число', previous_number)
next_number = number + 1
print('После числа', number, 'идет число', next_number)
===================================================================================================
print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2
cathetus_1 = int(input('Введите длину первого катета : '))
cathetus_2 = int(input('Введите длину второго катета : '))
area = (cathetus_1 * cathetus_2) / 2
print(area)
===================================================================================================
print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.
minutes = int(input('Введите колличество минут: '))
hours = minutes // 60
rest_minutes = minutes - (hours * 60)
print(hours, 'часов и', rest_minutes, 'минут')
===================================================================================================
print('Задача 6')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
result = (first_number % 100) + (second_number % 100)
print(result)
===================================================================================================
print('Задача 7. Поездка по кругу')

# Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
# Длина дороги — 115 километров.
# Вася стартует с нулевого километра и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?
#
# Реализуйте программу,
# которая спрашивает у пользователя v и t,
# и выводит целое число от 0 до 114 — номер километра, на котором остановится Вася.
# Учтите, что он может прокатиться больше одного круга.
circle = 115
print('1 круг равен', circle, 'киллометров')
speed = int(input('Введите скорость: '))
time = int(input('Введите колличество часов: '))
full_circle = (speed * time) // circle
finish = (speed * time) - (full_circle * 115)
print('Вы остановитесь через', full_circle, 'круга(ов) на', finish, 'киллометре')
===================================================================================================
print('Задача 8. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных
number = int(input('Введите четырехзначное число: '))
number1 = number % 10
number2 = (number // 10) % 10
number3 = ((number // 10) // 10) % 10
number4 = (((number // 10) // 10) // 10) % 10
print(number1, number2, number3, number4)
===================================================================================================
print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.
number = int(input('Введите четырехзначное число: '))
number1 = number % 10
number2 = (number // 10) % 10
number3 = ((number // 10) // 10) % 10
number4 = (((number // 10) // 10) // 10) % 10
print(number1 * 1000 + number2 * 100 + number3 * 10 + number4)
===================================================================================================
print('Задача 10. Поменять местами: не всё так просто! (необязательная, повышенной сложности)')

# Мы умеем менять местами строковые переменные и знаем,
# что в переменных, кроме строк, можно хранить и числа.
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и без использования  синтаксического сахара,
# который мы разбирали, а именно — без конструкции a,b = b,a.
# В переменные будут вводиться только числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# Изменять, удалять, менять местами 10-ю, 11-ю, 12-ю и 14-ю строчки нельзя.
# Но в 13-ю строку можно вставлять сколько угодно кода, не трогая последний принт.
===================================================================================================
