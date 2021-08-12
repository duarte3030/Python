# 13. Write a Python program to extract digits from given string
# a = ''.join(filter(lambda i: i.isdigit(), test_string))
# print(a)

test_string = "1a2d3h4a5r6a"
num_string = ""
for i in range(len(test_string)):
    if test_string[i].isdigit():
        num_string += str(test_string[i])
print(num_string)
