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
def first_n_text(s, n):
    if len(s) < n:
        return s
    else:
        return s[:n]
text = input("введіть рядок: ")
n = int(input("кількість символів: "))
print(first_n_text(text, n))



