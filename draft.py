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








