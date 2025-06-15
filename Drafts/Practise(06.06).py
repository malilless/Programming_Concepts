# line = input("Enter a line")
# try:
#     number = int(line)
#     print(number)
# except ValueError:
#     print("It's a text line")

# my_string = "Python"
# try:
#     print(my_string[10])
# except IndexError:
#     print("Спроба доступу за межі рядка!")

# a = input("Enter a number: ")
# b = input("Enter one more number: ")
# try:
#     print(sum(a,b))
#     print(a-b)
#     print(a*b)
#     print(a/b)
# except TypeError:
#     with open("File.txt", "a+") as f:
#         f = f.write("An Error occured")

# with open('file.txt', 'a+') as f:
#     f.write('0')

# while True:
#     try:
#         input_list = []
#         for i in range(0,2):
#             user_input = input(f"Enter number #{i}:")
#             input_list.append(user_input)
#             # sum
#             print(sum(input_list))
#             break
#     except Exception as e:
#         with open("error_log.txt", "a+") as f:
#             f.write(str(e) +"\n")
#             print("помилку записано")

