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

