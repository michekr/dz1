name = input("ім'я: ")
age = input("вік: ")
print(f"Привіт {name}, тобі {age}!")


age = int(input(" вік: "))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

start = int(input(" початкове число: "))
end = int(input(" кінцеве число: "))

for i in range(start, end + 1):
    print(i)

n = int(input("число дя обчислення факторіалу: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} = {factorial}")