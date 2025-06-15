# Task 1
# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     print(content)
#     list = []
#     list = content.split("\n")
#     print(list)
# with open("numbers.txt", "w") as f:
#     for i in list:
#         if int(i)%2 == 0:
#             f.writelines(i + "\n")


# Task 2
# with open('Ukrainian Modern History Syllabus 2024.txt', 'r', encoding="utf-8") as f:
#     content = f.read()
#     print(content)
# lower_content = content.lower()
# print(lower_content)
# punctuation_list = [",", ".", "*", ":", "-", ";", "?", "!", "...", ")", "("]
# for i in punctuation_list:
#     lower_content.replace(i, " ")
# all_words_list = lower_content.split()
# unique_words_set = set(all_words_list)
# frequiency_dict = {}
# for i in unique_words_set:
#     frequiency_dict[i]=all_words_list.count(i)
# print(frequiency_dict)

# with open('Ukrainian Modern History Syllabus 2024.txt', 'r', encoding="utf-8") as f:
#     content = f.read().lower().split()
#     print(content)

# Task 3
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data)
# print(data["title"])
# print(data["body"])

