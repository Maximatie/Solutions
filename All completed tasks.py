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
print('Задача 1. Датчик погоды')

# В квартире стоит датчик погоды за окном
# , который определяет, идёт дождь или нет.
# Если пошёл дождь, датчик оповещает владельцев сообщением: «Пошёл дождь. Возьмите зонтик!»
# Напишите программу,
# которая получает на вход число 0 или 1.
# Единица означает, что дождь идёт.
# Если дождь идёт, то выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!».

# Пример:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет =)
print('1 - дождь идёт, 2 - дождя нет')
rain = int(input('На улице идет дождь ?: '))
if rain == 1:
    print('Пошел дождь , возьмите зонтик!')
else:
    print('На улице отличная погода !')
===================================================================================================
print('Задача 2. Поступление')

# Степан хочет поступить на бюджет в престижный университет,
# но для этого ему нужно хорошо сдать три экзамена и набрать как минимум 270 баллов.
# Напишите программу,
# которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам
# и проверяет, поступил он в институт или нет.
# Выведите соответствующее сообщение.

# Пример:
# Введите кол-во баллов по русскому языку: 90
# Введите кол-во баллов по математике: 90
# Введите кол-во баллов по информатике: 90
# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите кол-во баллов по русскому языку: 100
# Введите кол-во баллов по математике: 50
# Введите кол-во баллов по информатике: 70
# К сожалению, ты не прошёл на бюджет.
mathematics = int(input('Введите кол-во баллов по математике: '))
language = int(input('Введите кол-во баллов по русскому языку: '))
informatics = int(input('Введите кол-во баллов по информатике: '))
if mathematics + language + informatics >= 270:
    print('Поздравляем , вы поступили на бюджет')
else:
    print('К сожалению , вы не поступили на бюджет')
===================================================================================================
print('Задача 3. Следим за зубами')

# Стоматолог посоветовал Маше использовать зубную нить каждый чётный день.
# Чтобы не забывать, Маша написала скрипт на Python,
# который в случае чего напоминает ей про совет стоматолога.
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение.
# Подсказка: для проверки чётности используйте оператор %.
number = int(input('Введите число: '))
if number % 2 == 0:
    print("Число является четным")
else:
    print('Число нечетное!')
===================================================================================================
print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть.
# Вот для одного из таких магазинов он и написал калькулятор скидки,
# чтобы проще ориентироваться в ценах.

# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100).
# В конце вывести итоговую сумму на экран.
product1 = int(input('Введите первую стоймость товара: '))
product2 = int(input('Введите вторую стоймость товара: '))
product3 = int(input('Введите третью стоймость товара: '))
full_price = product1 + product2 + product3
discount = (full_price // 100) * 90
if full_price > 10000:
    print('Стоймость товаров с учетом скидки', discount, 'руб.')
else:
    print('Стоймость товаров', full_price, 'руб.')
===================================================================================================
print('Задача 5. Модуль числа')

# Математик Саша пишет программу, которая должна строить график функции y = |x|.
# Для этого ему нужно находить модуль очередного числа x,
# то есть если число x отрицательное, то переводить его в положительное.
# Напишите программу, которая выводит на экран модуль введённого числа.
#
# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7
#
# Подсказка: достаточно в некоторых случаях переприсвоить переменную со знаком минус.
number = int(input('Введите число: '))
if 0 > number:
    print(number * -1)
else:
    print(number)
===================================================================================================
print('Задача 6. Игра в кубики')

# Костя играет в азартную игру с кубиками с владельцем заведения.
# Правда, с довольно интересными правилами:
# если у Кости на кубике выпадет столько же или больше, чем у владельца,
# то Костя задолжает разность в тысячах долларов.
# Однако если выпадет меньше,
# то Косте выплатят столько тысяч долларов, сколько будет в сумме очков на кубиках.

# На вход в программу подаётся два числа.
# Если первое число больше либо равно второму,
# нужно вывести на экран их разность и отдельной строкой фразу: «Костя платит».
# В противном случае вывести их сумму и отдельной строкой — фразу: «Владелец платит».
# Также последней строкой в результате нужно вывести на экран фразу: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена
kostyas_cube = int(input('Кубик кости: '))
owners_cube = int(input('Кубик владельца: '))
lose_game = kostyas_cube - owners_cube
win_game = kostyas_cube + owners_cube
if kostyas_cube >= owners_cube:
    print('Костя платит:', lose_game)
else:
    print('Владелец платит', win_game)
print('Игра окончена')
===================================================================================================
print('Задача 7. Банкомат')

# Пользователи банкомата хотят снимать деньги.
# Но банкомат умеет выдавать только купюры по 100 рублей.
# Напишите программу,
# которая проверяет допустимость суммы средств, которую ввёл пользователь.

# Пример:
# Введите сумму, которую хотите снять: 250
# Такую сумму снять невозможно. Обратитесь в другой банкомат.
money = int(input('Введите сумму которую хотите снять: '))
if money % 100 == 0:
    print('Заберите деньги')
else:
    print('Обратитесь в другой банкомат')
===================================================================================================
print('Задача 8. Тяжёлая жизнь')

# Георгий работает по часам и неофициально
# на какой-то сомнительной работе,
# на которой его зарплата высчитывается по следующей формуле:
# 200 * hours / 2 ** 3 + hours

# Он хочет понять, сколько часов нужно отработать,
# чтобы хватило на погашение кредита и на еду.

# Напишите программу,
# которая запрашивает у пользователя три числа:
# количество отработанных часов,
# остаток по кредиту и количество денег на еду.
# После этого рассчитывается зарплата по формуле,
# и если зарплата больше либо равна сумме денег на кредит и еду,
# то выводится сообщение: «Часов хватает. Можно отдохнуть»,
# в противном случае: «Часов не хватает. Придётся работать!».

# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся поработать!
hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите расходы на еду: '))
salary = 200 * hours / 2 ** 3 + hours
if credit + food >= salary:
    print('Часов не хватает. Придётся работать!')
else:
    print('Часов хватает. Можно отдохнуть')
===================================================================================================
print('Задача 9. Плохой циферблат')

# У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега,
# но он постоянно глючит и сбрасывается.
# Саша заметил закономерность:
# каждый раз, когда сумма цифр на циферблате превышает число текущего дня,
# циферблат сбрасывается.

# Напишите программу,
# которая получает на вход от пользователя два числа: пробег и номер дня (первое — обязательно трёхзначное),
# затем находит сумму цифр первого числа,
# и если эта сумма больше второго числа,
# выводит сообщение: «Сброс», — и сбрасывает пробег до нуля.
# В противном случае выводится: «Сегодня не сломался».
# В конце также выводится сам пробег.
mileage = int(input('Пробег(трехзначное число): '))
clock_face = int(input('Число текущего дня: '))
number3 = mileage % 10
number2 = (mileage // 10) % 10
number1 = mileage // 100
sum_of_numbers = number3 + number2 + number1
if sum_of_numbers > clock_face:
    print('Сброс, пробег сброшен с', clock_face, 'до', clock_face * 0)
else:
    print('Сегодня не сломался', clock_face)
===================================================================================================
print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
max_number = number1
if max_number < number2:
    max_number = number2
if max_number < number3:
    max_number = number3
print(max_number)
===================================================================================================
print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.

number = int(input('До какого числа возводим ? '))
startNumber = 0
radical = 1
while startNumber != number:
    print(radical ** 3)
    radical += 1
    startNumber += 1
===================================================================================================
print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

name = input('Как вас зовут ? ')
debt = int(input('Сумма вашего долга : '))
print(name, 'ваша задолженность составляет', debt, 'рублей')
money = int(input('Сколько рублей вы внесете прямо сейчас, чтобы её погасить? '))
while money < debt:
    print('Маловато,', name, '. Давайте еще раз.')
    money = int(input('Сколько рублей вы внесете прямо сейчас, чтобы её погасить? '))
    if money >= debt:
        print('Отлично', name, '! Вы погасили долг. Спасибо!')
===================================================================================================
print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.

# Напишите программу,
# которая считала бы для него,
# сколько десятичных цифр (знаков) во вводимом числе.

number = int(input('Введите число:'))
count = 0
while number >= 1:
    number //= 10
    count += 1
print(count)
===================================================================================================
print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей.
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.

# Напишите программу,
# которая считает количество только чётных чисел в последовательности
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.
number = int
even_number_count = 0
while number != 0:
    number = int(input('Введите число: '))
    if number == 0:
        break
    elif number % 2 == 0:
        print('Число четное!')
        even_number_count += 1
    else:
        print('Число нечетное!')
print('Введено четных чисел:', even_number_count)
===================================================================================================
print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

ticket_number = int(input('Введите номер билета: '))
if ticket_number // 100000 + (ticket_number // 10000 % 10) + (ticket_number // 1000 % 10) == (ticket_number % 1000 //
        100) + (ticket_number % 1000 // 10 % 10) + ticket_number % 10:
    print('Поздравляем, у вас счастливый билет !')
else:
    print('К сожалению , ваш билет не счастливый.')
===================================================================================================
print('Задача 6. Поставьте оценку!')

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению от −100 до 100.
# Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.

# Напишите программу,
# которая находит количество положительных
# и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.

# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

number = int
negative_number = 0
positive_number = 0
while number != 0:
    number = int(input('Введите число: '))
    if 100 > number > 0:
        positive_number += 1
    elif -100 < number < 0:
        negative_number += 1
    else:
        break
print('Кол-во положительных чисел:', positive_number)
print('Кол-во отрицательных чисел:', negative_number)
===================================================================================================
print('Задача 7. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин

hour = 1
print('Начался 8-часовой рабочий день.')
print(hour, '-й час')
tasks_count = 0
calls_count = False
while hour != 9:
    task = int(input('Сколько задач решит Максим? '))
    tasks_count += task
    call = int(input('Звонит жена. Взять трубку? (1-да, 0-нет)'))
    if call == 1:
        calls_count = True
    hour += 1
    print(hour, '-й час')
print('Рабочий день закончился. Всего выполнено задач:', tasks_count)
if calls_count:
    print('Нужно зайти в магазин.')
===================================================================================================
print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
money = float(input('Введите сумму вклада: '))
procent = float(input('Введите процент: '))
finall_money = float(input('Укажите нужную сумму: '))
years = 0
while money < finall_money:
    money += money / 100 * procent
    years += 1
    if money >= finall_money:
        break
print('Для достижения необходимой суммы, вам необходим вклад на ', years, 'лет')
===================================================================================================
print('Задача 9. Игра «Угадай число»')

# В одном из домашних заданий мы делали задачу,
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том,
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число.
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.

# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4
number = int
number_count = 0
while number != 7:
    number = int(input('Введите число: '))
    number_count += 1
    if number > 7:
        print('Число больше чем необходимо! Попробуйте еще раз!')
    elif number < 7:
        print('Число меньше чем необходимо! Попробуйте еще раз!')
    else:
        print('Вы угадали! Число попыток: ', number_count)
===================================================================================================
print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

print('Загадайте число от 1 до 100!')
low = 0
high = 100
while True:
    search = (high + low) // 2
    print('Вы загадали число', search, '?')
    answer = int(input("Введите '1' если я угадал. Введите '2' если ваше число больше . Введите '3' "
                       "если выше число меньше. "))
    if answer == 3:
        high = search
    elif answer == 2:
        low = search
    elif answer == 1:
        print("Игра окончена. Вы загадали число:", search)
        break
    else:
        print("Извините , введенное значение некорректно.")
===================================================================================================
print('Задача 1. Тайны археологии')

for number in 114, 12, 14, 10605, 4907, 450:
    if number % 3 != 0 and number % 2 == 0:
        print(number, '- подходит.')
    else:
        print(number, '- не подходит.')
===================================================================================================
print('Задача 2. Должники')

positive_number = 0
for numbers in range(0, 11):
    number = int(input('Введите число: '))
    if number > 0 and number % 2 == 0:
        positive_number += 1
print(positive_number, 'чисел являются одновременно положительными и четными.')
===================================================================================================
print('Задача 3. Посчитай чужую зарплату...')

total_salary = 0
for month in range(1, 13):
    total_salary += int(input("Введите зарплату за месяц: "))
total_salary //= 12
print('Ваша средняя зарплата за год равна', total_salary, 'рублей')
===================================================================================================
counter = 0
for sector in range(30, 36):
    people_in_sector = int(input('Сколько людей в ' + str(sector) + ' секторе? : '))
    if people_in_sector > 10:
        counter += 1
        print('Тревога, слишком много людей в секторе!')
    elif 0 < people_in_sector <= 10:
        print('Все спокойно.')
    else:
        print('Ошибка введенных данных !')
print('Нарушений выявлено: ', counter)
===================================================================================================
print('Задача 5. Факториал')

start_result = 1
number = int(input('Введите число, факториал которого необходимо найти: '))
for start_number in range(1, number + 1):
    start_result *= start_number
print('Факториал числа', number, 'равен', start_result)
===================================================================================================
