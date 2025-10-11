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