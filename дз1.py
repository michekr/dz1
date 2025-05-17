#1
name = input("ім'я: ")
age = input("вік: ")
print(f"Привіт {name}, тобі {age}!")

#2
age = int(input(" вік: "))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")
#4
start = int(input(" початкове число: "))
end = int(input(" кінцеве число: "))

for i in range(start, end + 1):
    print(i)
#6
n = int(input("число дя обчислення факторіалу: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} = {factorial}")
#7
score = int(input("бали: "))

if 0 <= score <= 49:
    print("Незадовільно.")
elif 50 <= score <= 69:
    print("Задовільно.")
elif 70 <= score <= 89:
    print("Добре.")
elif 90 <= score <= 100:
    print("Відмінно.")
else:
    print("Некоректна кількість балів.")