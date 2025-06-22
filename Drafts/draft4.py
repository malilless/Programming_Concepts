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


#Task 2
import sys
with open('Ukrainian Modern History Syllabus 2024.txt', 'r', encoding="utf-8") as f:
    content = f.read()
    #print(content)
content = content.lower()
#print(lower_content)
punctuation_list = [",", ".", "*", ":", "-", ";", "?", "!", "...", ")", "("]
for i in punctuation_list:
    content.replace(i, " ")
index = content.find("?")
if (index > -1):
    print(f"'?' found at {index}")
    if (index < 100): start = 0 
    else: start = index - 100
    print(f"...... {content[start:start + 1000]} ......")
sys.exit()

all_words_list = content.split()
unique_words_set = set(all_words_list)
frequiency_dict = {}
for i in unique_words_set:
    frequiency_dict[i]=all_words_list.count(i)
print(frequiency_dict)

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
