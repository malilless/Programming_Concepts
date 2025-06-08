print("Початковий рівень")
print("Завдання 1:")
numbers_list = [1,3,65,8,4,32,13,7]
total_sum = sum(numbers_list)
print(f"Сума чисел у списку: {total_sum}.")

print("Завдання 2:")
numbers_list = [1,3,65,8,4,32,13,7]
minimum = min(numbers_list)
print(f"Мінімум у списку: {minimum}.")

print("Завдання 3:")
numbers_list = [1,3,65,8,4,32,13,7]
reverse = numbers_list[::-1]
print(f"Реверс списку: {reverse}.")

print("Завдання 4:")
numbers_list = [1,3,65,8,4,32,13,7]
for i in numbers_list:
    if i % 2 != 0:
        print(f"Непарні числа зі списку: {i}.")
    else:
        continue

print("Завдання 5:")
numbers_list = [1,3,65,8,4,32,13,7]
x = int(input("Введіть x: "))
for i in numbers_list:
    print(f"Список чисел, помножених на x: {i*x}.")

print("Легкий рівень")
print("Завдання 1:")
numbers_list = [1,3,65,8,4,32,13,7]
x = int(input("Введіть x: "))
greater_than_x = [i for i in numbers_list if i > x]
print(f"Числа, більші за x: {greater_than_x}.")

print("Завдання 2:")
numbers_list_2 = [1,3,-1,65,8,-40,4,32,13,7]
positive_numbers = [i for i in numbers_list if i > 0]
print(positive_numbers)
average = sum(positive_numbers)/len(positive_numbers)
print(f"Середнє додатних чисел: {average}.")

print("Завдання 3:")
not_sorted = [2,4,5,6,3,8,9,]
x = int(input("Введіть x: "))
sorted = [i for i in not_sorted if i < x]
print(sorted)
print(f"Відповідь: {max(sorted)}.")
#Завдання поставлено трохи некоректно: незрозуміло, шукати максимальне значення у відфільтрованому
#списку, чи значення, яке зустрічається у ньому найбільшу кількість разів...

print("Завдання 4:")
numbers_list = [1,3,65,8,4,32,13,7]
y = int(input("Введіть y: "))
divided_by_y = [i for i in numbers_list if i % y == 0]
print(divided_by_y)
sum = sum(divided_by_y)
print(f"Агрегована умовна сума: {sum}.")

print("Завдання 5:")
numbers_list = [1,3,65,8,4,32,13,7]
doubled = [i**2 for i in numbers_list]
print(f"Список квадратів: {doubled}.")

print("Завдання 6:")
numbers_list_2 = [1,3,-1,65,8,-40,4,32,13,7]
positive_numbers = [i for i in numbers_list if i > 0]
print(f"Витяг додатних чисел: {positive_numbers}.")

print("Завдання 7:")
words_list = ["підхід", "яблуко", "під'їзд", "картинка"]
with_prefix = [i for i in words_list if i.startswith("під")] #Bбудовану функцію startswith я знайшла в інтернеті
print(f"Рядки з префіксом: {with_prefix}.")

print("Завдання 8:")
numbers_list = [1,3,65,8,4,32,13,7]
while True:
    N = int(input(f"Введіть N від 1 до {len(numbers_list)}: "))
    if N > len(numbers_list) or N < 1:
        print(f"N має бути в діапазоні: (1,{len(numbers_list)})")
    else:
        break
sum = 0
for i in range(0,N):
    sum+=numbers_list[i]
print(f"Сума перших N чисел: {sum}.")

print("Завдання 9:")
list = ["я", "карта", "вижив", "алала"]
palindromes = [i for i in list if i==i[::-1]]
print(f"Всі паліндроми: {palindromes}.")

print("Завдання 10:")
numbers_list = [1,3,65,8,4,32,13,7]
divider = int(input("Введіть дільник: "))
check_list = []
for i in numbers_list:
    if i % divider == 0:
        check_list.append("ділиться")
    else:
        check_list.append("не ділиться")
print(f" Перевірка подільності: {check_list}.")

print("Середній рівень")
print("Завдання 1:")
numbers_list_3 = [2,3,6,9,10,12,15]
x = int(input("Введіть x: "))  
y = int(input("Введіть y: "))
another_list = [i for i in numbers_list_3 if i % x == 0 and i % y != 0]
print(f"Числа, які діляться на X, але не діляться на Y: {another_list}.")
# Роботу цього коду буде класно видно, якщо ввести х=2, а у=3

print("Завдання 2:")
list_of_lists = [[1,2,3,4], [5,6,7], [9,0,7,1]]
new_list = []
for list in list_of_lists:
    for i in list:
        new_list.append(i)
print(f"Єдиний список: {new_list}.")

print("Завдання 3:")
phrases = ["I wAnnA wAtCh MuLan fOr 123446454 tImE", "I NEED my EurovisioN wEEk BACK!:("]
capital_letters = []
for phrase in phrases:
    for letter in phrase:
        if letter.isupper(): #Isupper теж шукала в інтернеті
            capital_letters.append(letter)
print(f"Великі літери в підрядках: {capital_letters}.")

print("Завдання 4:")
numbers_list = [1,3,3,6,8,1,4,3,3,7,4,4]
frequency_dict = {}
print(f"Оригінальний список:{numbers_list}")
numbers_list.sort(reverse=True)
print(f"Відсортований за спаданням: {numbers_list}")
for number in numbers_list:
    print(f"Шукаємо '{number}' в словнику.")
    if number in frequency_dict:
        print(f"'{number}' знайдено в словнику. Значення: {frequency_dict[number]}. Збільшуємо його на 1.")
        frequency_dict[number] += 1
    else:
        print(f"'{number}' НЕ знайдено в словнику. Задаємо значення 1.")
        frequency_dict[number] = 1
    print(f"Словник: {frequency_dict}")
frequency_dict_sorted = dict(sorted(frequency_dict.items(), key=lambda tuple: tuple[1], reverse=True))
print(f"Відсортований словник: {frequency_dict_sorted}")
list_by_freq = []
for number, count in frequency_dict_sorted.items():
    for i in range(0,count):
        list_by_freq.append(number)
print(f"Список, відсортований за частотою: {list_by_freq}.")
#Знову-ж, не дуже зрозуміла умова + довелося скористатися допомогою тата-програміста та інтернету, 
#бо, наскільки я пам'ятаю, ми не вчилися сортувати словники і працювати з лямбдами

print("Завдання 5:")
list1 = [2,4,5,6,7,7]
list2 = [1,8,5,6,2,9]
if len(list1) == len(list2):
    print(f"Об'єднаний список: {list1 + list2}.")
else:
    print(f"The lists have different length!")

print("Завдання 6:")
dict1 = {
    "value1" : 22,
    "value2" : 13,
    "value3" : 7
}
sum_of_values = sum(dict1.values())
print(f"Агрегація словника: {sum_of_values}.")

print("Завдання 7:")
numbers_list = [1,3,65,8,4,32,13,7]
for i in range(len(numbers_list)):
    if i > 2:
        numbers_list[i] *= 10
print(f"Список із заміненими елементами: {numbers_list}.")

print("Завдання 8:")
list_of_rows = ["Kyle Alessandro", "Taylor Swift", "Choi Beomgyu"]
x = int(input("Введіть x: ")) 
rows_longer_than_x = []
for i in list_of_rows:
    if len(i) > x:
        rows_longer_than_x.append(i)
    else:
        continue
print(f"Кількість рядків, довших за x: {len(rows_longer_than_x)}.")

print("Завдання 9:")
lyrics1 = ["And I do not want the world", "When you are young", "I will be"]
lyrics2 = ["to see me", "they assume you know nothing", "my own lighter"]
print(f"Рядок 1: {lyrics1[0] + " " + lyrics2[0]}.")
print(f"Рядок 2: {lyrics1[1] + " " + lyrics2[1]}.")
print(f"Рядок 3: {lyrics1[2] + " " + lyrics2[2]}.")
# Source: "Iris" by Goo Goo Dolls, "cardigan" by Taylor Swift, "Lighter" by Kyle Alessandro:)

print("Завдання 10")
numbers_list = [1,3,65,8,4,32,13,7]
x = int(input("Введіть x: "))
y = int(input("Введіть y: "))
multiplied_by_y = [i*y for i in numbers_list if i > x]
print(f"Список чисел (більших за x) помножених на y: {multiplied_by_y}.")
   