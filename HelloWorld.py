print("Завдання 1")
x = "Hello, Python World!"
print(x)

print("Завдання 2")
y = int(input("Введіть число: ")) 
z = int(input("Введіть інше число: "))
print(y + z)
print(y - z)
print(y * z)
print(y / z)

print("Завдання 3")
row1 = "Привіт!"
row2 = "Як справи?"
full_row = row1 + " " + row2
print(full_row)

print("Завдання 4")
a = int(input("Введіть ще якесь число:> : "))
if a % 2 == 0:
    print("Парне")
else:
    print("Непарне")

print("Завдання 5")
for i in range(1,11,1):
    print(i)

print("Завдання 6")
num = int(input("І ще одне число, шо ж таке: "))
if num > 0:
    print("Позитивний")
elif num == 0:
    print("Дорівнює нулю")
else:
    print("Негативний")

print("Завдання 7")
for i in range(2,11,2):
    print(i)

print("Завдання 8")
n = int(input("Введіть число n: "))
for i in range(1,n,1):
    n += 1

print("Завдання 9")
for i in range(10,0,-1):
    print(i)

print("Завдання 10")
for i in range(11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)