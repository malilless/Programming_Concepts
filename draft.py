print("Завдання 8")
n = int(input("Введіть число n: "))
for i in range(1, n + 1, 1):
    n += 1
print(n)

print("Завдання 9")
for i in range(10,0,-1):
    print(i)

print("Завдання 10")
for i in range(1,116,1):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)