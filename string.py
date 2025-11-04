# # 1. Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок у верхньому і нижньому регістрах.
# print("QWERRdfgd34".lower())
# print("QWERRdfgd34".upper())
# print("QWERRdfgd34".isdigit())

# # 2. Скласти програму, яка запитує назву баскетбольної команди і повторює її на екрані зі словами: This is a champion!.
# name = input("Name: ")
# print(name + " OksanaThis is champion")

# "3. Дано натуральне число. Знайти число, що отримується при прочитанні його цифр справа наліво.
# def reverse_digits_str(n):
#     return int(str(n)[::-1])
# print(reverse_digits_str(12345))

# n = input("input number: ")
# print(int(str(n)[::-1]))

# 4. Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими. (метод 's.title()')
# s = "Ho ho ho ho HO"
# print (s.title())

# 5. Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.
# text = input("Введіть рядок: ")
# letter = input("Введіть літеру для пошуку: ")
# index = text.find(letter)
# if index != -1:
#     print("Порядковий номер літери:", index + 1)  
# else:
#     print("лірера відсутня у цьому рялку")

# # ------------------------------
# # 8 task
# ex = input("Enter ex:\n")  # 5-3+1
# # len_ex = len(ex)  # 5
# # n = (len(ex) + 1) // 2  # кількість цифр

# # 1 var
# # print(int(ex[0]) + (1 if ex[1] == "+" else -1) * int(ex[2]) + (1 if ex[3] == "+" else -1) * int(ex[4]))

# # 2 var
# # sum = int(ex[0])
# # for i in range (1, len(ex), 2):
# #     sum += (1 if ex[i] == "+" else -1) * int(ex[i+1])

# # print(sum)

# # 3 var
# # sum = int(ex[0])
# # for i in range(1, len(ex)):
# #     if ex[i] == "+":
# #         sum += int(ex[i+1])
# #     elif ex[i] == "-":
# #         sum -= int(ex[i+1])
# # print(sum)

# # 4 var
# #--------------------------
# # my_list = ["1", "2", 4, 7]
# # for el in range(len(my_list)):
# #     my_list[el] = str(my_list[el])
# # print(my_list)

# # new_list = list(map(int, my_list))
# # print(new_list)
# #-----------------------------------------------

# ex = ex.replace("-", "+-")
# parts = ex.split("+")

# # map()
# sum_ex = sum(map(int, parts))
# print(sum_ex)