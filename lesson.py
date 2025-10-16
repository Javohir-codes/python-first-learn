# print(a+number) # плюс
# print(a-number) # минус
# print(a*number) # умножение
# print(a/number) # деление
# print(a//number) # деление без остатков
# print(a**number) # степень
# print(a%number) # остаток
# print(a==number) # сравнение
# print(a>number) # сравнение
# print(a<number) # сравнение

# print("Hello: ", "Ja", "vo", "hir", sep="!", end=". .")
# print("Second Text", end="\n")
# print("Third \" Text\"")
# print('Fourth \t \\ Text')
# print(min(1, 0, -5, -1, 3))
# print(max(1, 0, -5, -1, 3))
# print(abs(-5))
# print(pow(5, 3)) #степень
# print(round(5 / 3)) #деление к более ближающему



# user_number = int(input("Guess a Number From 1 to 9 And Place It: "))

# if user_number == 5:
#     print("Yes, It's True Number Is", end=" ")
#     print(user_number)
# elif user_number > 9:
#     print("No, We Need Number From 1 To 9")
# elif user_number != 5:
#     print("Number Isn't", end=" ")
#     print(user_number)



# for test in range(2, 20, 1):
#     if test == 10:
#         break
#     if test % 2 == 0:
#         continue
#     print(test)



# for hi in word:
#     print(hi * 3)



# word = "Javohir"

# count = 0
# for i in word:
#     if i == "a":
#         count += 1
# print("Count", count)



# number = 5

# while number <= 15:
#     print(number)
#     number += 2



# test = True

# while test:
#     if input("Enter Data: ") == "Stop":
#         test = False



# found = None

# for rm in "Hello World":
#     if rm == "l":
#         found = True
#         break
# else:
#     found = False

# print(found)



# nums = [123, True, "Hello", 3.14, [1234, 5678]]
# nums[0] = 555
# nums.append(100)
# nums.insert(2, "Hi")
# b = [1, 2, 3]
# nums.extend(b)
# nums.reverse()
# nums.pop(7)
# nums.remove(1)
# nums.clear()
# print(nums)



# n = int(input("Enter Lenght: "))
# user_list = []
# i = 0
# while i < n:
#     string = "Enter Element №0" + str(i + 1) + ":"
#     user_list.append(input(string))
#     i += 1
# print(user_list)



# Word = "sos academy"
# print(Word[::2])
# print(len(random))
# print(random.upper())
# random = Word.split(" ")
# for i in range(len(random)):
#     random[i] = random[i].capitalize()

# print(random)



# country = {"code": "UZ", "name": "Uzbekistan", "population": "12"}
# for key, value in country.items():
#     print(key, " - ", value)


# func = lambda a, b: a + b
# res = func(5, 9)
# print(res)

# nums = [11, 6, 5, 7, 3, 8, 9]
# min = min_number(nums)
# minimum = nums[0]

# def minimal(list):
#     min_number = list[0]
#     for el in list:
#         if el < min_number:
#             min_number = el
# print(min_number)



# Lesson 2
# test = ["Hello", 123, True, 3.14]
# print(test[0])
# print(float(5))
# a = "Javohir"
# print(a.upper())
# print("a, b, c".split(","))
# print("123 ".strip().isdigit())
# print("hello ".strip().isalpha())



# Calculator

# number_1 = int(input("Place First Number: "))
# number_2 = int(input("Place Second Number: "))
# Operator = input("Place The Operator: ")
# if Operator == "+":
#     print(number_1 + number_2)
# elif Operator == "-":
#     print(number_1 - number_2)
# elif Operator == "/":
#     print(number_1 / number_2)
# elif Operator == "*":
#     print(number_1 * number_2)
# elif Operator == "%":
#     print(number_1 % number_2)
# elif Operator == "//":
#     print(number_1 // number_2)
# elif Operator == "**":
#     print(number_1 ** number_2)



# original = "[INFO] User: alice Status: OK"

# level = original.split(" ")[0]
# username = original.split(" ")[2].capitalize()
# status = original.split(" ")[-1]

# print(level)
# print(username)
# print(status)

# test = input("Place text: ")
# name = "ab"
# if test == name:
#     print("True")




# films = []
# films.append("Человек Паук Нет Пути Домой")
# films.insert(0, "Random")
# films.remove("Random")

# print(films)


# queue = ["Алиса", "Боб", "Чарли"]
# queue.append("Давид")
# queue.insert(1, "Элина")
# queue.pop(0)
# queue.remove("Боб")

# print(queue)


# cart = ["телефон", "наушники"]
# cart.extend(["чехол", "зарядка"])
# cart.pop(3)
# cart.insert(0, "ноутбук")

# print(cart)


# tasks = []
# print("Введите 3 Задачи")
# a = input("Введите 1-ую задачу: ")
# b = input("Введите 2-ую задачу: ")
# c = input("Введите 3-ую задачу: ")

# tasks.append(a)
# tasks.append(b)
# tasks.append(c)

# tasks.pop(2)

# print("Проверить почту")
# print(tasks)


# colors = ["красный", "синий", "зелёный"]
# colors.extend(["жёлтый", "оранжевый"])
# colors.append("серый")
# colors.remove("серый")

# print(colors)



# result = [
#  ("Макс Ферстаппен", "Red Bull", 1),
#  ("Льюис Хэмилтон", "Mercedes", 2),
#  ("Никто")
# ]
# гонщик = ("Ландо Норрис", "McLaren", 5)
# result.append(("Шарль Леклер", "Ferrari", 3))
# result.append(гонщик)

# first = "1-Place"
# second = "2-Place"
# third = "3-Place"
# fourth = "4-Place"
# fifth = "5-Place"

# print(first, ": ", result[0])
# print(second, ": ", result[1])
# print(third, ": ", result[2])
# print(fourth, ": ", result[3])
# print(fifth, ": ", result[4])


# инфо1 = ("Оскар Пиастри",)
# инфо2 = ("McLaren", 6)

# print(инфо1 + инфо2)


# команды = ("Red Bull", "Ferrari", "Mercedes", "Red Bull", "McLaren", "Ferrari", "Red Bull")
# print(команды.count("Red Bull"))
# print(команды.index("McLaren"))


# инопланетяне = [
#  ("Зоргон", "Нептурон", 3, True),
#  ("Блип", "Ксандар", 1, False),
#  ("Блип", "Ксандар", 1, True),
#  ("Момо", "Кеплер-22б", 2, True)
# ]

# alien1 = ("Зара", "Андромеда", 4, True)
# alien2 = ("Крогг", "Венера", 2, False)

# инопланетяне.pop(1)
# инопланетяне.append(alien1)
# инопланетяне.append(alien2)

# print(инопланетяне[0][0], end=" ")
# print(инопланетяне[0][2])

# print(инопланетяне[1][0], end=" ")
# print(инопланетяне[1][2])

# print(инопланетяне[2][0], end=" ")
# print(инопланетяне[2][2])

# print(инопланетяне[3][0], end=" ")
# print(инопланетяне[3][2])

# print(инопланетяне[4][0], end=" ")
# print(инопланетяне[4][2])


# планеты = ("Ксандар", "Нептурон", "Ксандар", "Кеплер-22б", "Ксандар") 
# print(планеты.count("Ксандар"))
# print(планеты.index("Кеплер-22б"))





# инопланетяне = [
#     ("Зоргон", "Нептурон", "3", True),
#     ("Блип", "Ксандар", "1", False),
#     ("Блип", "Ксандар", "1", True),
#     ("Момо", "Кеплер-22б", "2", True),
#     ("Крогг", "Венера", "2", False),
#     ("Зара", "Андромеда", "4", True)
# ]

# for name, planet, eyes, дружелюбный in инопланетяне:
#     eyes = int(eyes)
#     if дружелюбный and eyes > 2:
#         print(name, "Приятный многоглазик")
#     elif дружелюбный and eyes <= 2:
#         print(name, "Милый малыш")
#     else:
#         print("ОПАСНО! держитесь подальше от", name)


# курсы = {"Python", "Java", "C++", "JavaScript", "Go"}
# новые_курсы = {"Kotlin", "Swift", "TypeScript"}
# новые_курсы.add("Rust")
# курсы.update(новые_курсы)
# курсы.discard("C++")
# курсы.discard("Ruby")
# print(курсы)


# все_курсы = {}
# frontend = {"HTML", "CSS", "JavaScript", "React"}
# backend = {"Python", "Node.js", "Java", "SQL"}

# все_курсы = frontend | backend
# sort = sorted(все_курсы)

# print(все_курсы)
# print(sort)


# анна = {"Python", "JavaScript", "HTML"}
# борис = {"Java", "C++", "HTML"}

# both = анна & борис
# print("Оба проходили:", both)

# unique_anna = анна - борис
# print("Уникальные для Анны:", unique_anna)

# all = анна | борис
# print("Все курсы:", all)



# x = int(input("Введи число: "))

# if x > 0:
#     print("Положительное")
# elif x < 0:
#     print("Отрицательное")
# elif x == 0:
#     print("Ноль")


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))

# if a > b and a > c:
#     print("Самое большое:", a)
# elif b > a and b > c:
#     print("Самое большое:", b)
# else:
#     print("Самое большое:", c)

# if a < b and a < c:
#     print("Самое маленькое:", a)
# elif b < a and b < c:
#     print("Самое маленькое:", b)
# else:
#     print("Самое маленькое:", c)

# if a == b == c:
#     print("Все числа равны")