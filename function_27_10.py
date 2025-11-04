# 1. Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення `Hello, <name>`.
# def name_hello(name="Inkognito"):
#     return f"Hello, {name}!"
# name = "Oksana"
# print(name_hello())
# print(name_hello(name))

# 2. Напишіть функцію, яка отримує рядок і ціле число `n` та повертає `n` копій заданого рядка.
# def copy_str(text, n):
#     return (" " + text + " ")  * n
# text = input("введіть рядок: ")
# n = int(input("введіть кількість повторень: "))
# print(copy_str(text, n))

#3. Напишіть функцію для обчислення суми двох цілих чисел.
# def sum_a_b(a, b):
#     return a + b 
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# print(sum_a_b(num1, num2))

# 4. Напишіть функцію для отримання рядка з перших `n` символів іншого рядка. Якщо довжина рядка менше `n`, поверніть початковий рядок.
# def first_n_text(s, n):
#     if len(s) < n:
#         return s
#     else:
#         return s[:n]
# text = input("введіть рядок: ")
# n = int(input("кількість символів: "))
# print(first_n_text(text, n))

# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції `max()`.
def max_from_three(n1, n2, n3):
    return max(num1, num2, num3)
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
print(max_from_three(num1, num2, num3))

# 6. Напишіть функцію для створення позначок тегів `HTML` навколо введених рядків. Функція отримує назву тега `HTML` і рядок, який необхідно помістити у відповідні теги.
# strong Python
#     ```
#     Вихідні дані:
#     ```
#     <strong>Python</strong>
# def teg_htm(teg, text):
#     return f"<{teg}>{text}</{teg}>"
# text = input("Enter text:")
# teg = text.split()[0]
# string = " ".join(text.split()[1:])
# print(teg_htm(teg, string))

# def rainfall_statistic(values):
#     month = [
#              "January", "February", "March", "April", 
#              "May", "June", "July", "August", "September", 
#              "October", "November", "December"
#              ]
#     rain = list(map(float, values.split() ))
#     year_rainfall = sum(rain)
#     middle_year_rainfall = year_rainfall/12 #len(rain)
#     max_rain = max(rain)
#     max_month = month[rain.index(max_rain)]
#     min_rain = min(rain)
#     min_mounth = month[rain.index(min_rain)]
#     return (year_rainfall, middle_year_rainfall, (max_rain, max_month), (min_rain, min_mounth))

# data = "22 22 24 49 72 98 101 82 51 40 36 24"
# result = rainfall_statistic(data)
# print(result)

