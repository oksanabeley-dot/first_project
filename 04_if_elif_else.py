# Розгалудження

# 1. Напишіть програму, в якій користувач вводить пароль і 
# якщо він співпадає із наперед визначеним паролем для цього користувача, 
# то виводиться повідомлення Password accepted.. У іншому випадку 
# повідомлення буде Sorry, that is the wrong password..

password = input("Enter password: ")
password_accept = "PASSWORD"
if password == password_accept:
     print("Password accepted.")
else:
     print("Sorry, that is the wrong password.")



# 2. Користувачем вводиться два імені. Використовуючи конструкцію 
# розгалуження програма повинна вивести імена в алфавітному порядку.

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
if name1 <= name2:
     print(name1, name2)
else:
     print(name2, name1)


# 3. Напишіть програму, яка виводить назви введених чисел. Користувач 
# вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться 
# повідомлення - назва числа, відповідно, One, Two, Three. В усіх 
# інших випадках виводиться слово Unknown.

number = int(input("Enter number: "))
name_of_number = ""
if number == 1:
    name_of_number = "One"
elif number == 2:
     name_of_number = "Two"
elif number == 3:
     name_of_number = "Three"
else:
     name_of_number = "Unknow"

print(name_of_number)


# 4. Користувач вводить дві різних англійські літери в окремих рядках. 
# Напишіть програму, яка виводить повідомлення про місце розташування 
# однієї літери відносно іншої у алфавіті.

letter1 = input("Enter letter1: ").lower()
letter2 = input("Enter letter2: ").lower()

if letter1 <= letter2:
     print("First letter:", letter1, "Second letter:", letter2)
else:
     print("First letter:", letter2, "Second letter:", letter1)


# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

temperature = float(input("input temperature in oC  "))
if temperature <= 0:
     print ("A cold, isn’t it?")
elif temperature >0 and temperature<=10:
    print ("Cool")
elif temperature >30:
     print ("hot")
else:
     print ("Nice weather we’re having..")