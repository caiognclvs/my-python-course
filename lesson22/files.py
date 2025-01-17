import os

f = open('C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/names.txt')
# print(f.read())

for line in f:
    print(line)

f.close()

try:
    f = open("C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/context.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

f = open('C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/names.txt', "a")
f.write("Neil")
f.close()

f = open('C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/context.txt', "w")
f.write("New Text")
f.close()

# f = open("name_list.txt", "w")
# f.close()

# if not os.path.exists("dave.txt"):
#     f = open("dave.txt", "x")
#     f.close()

# if os.path.exists("dave.txt"):
#     os.remove("dave.txt")
# else:
#     print("The file you wish to delete doesn't exist")

with open('C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/more_names.txt') as f:
    content = f.read()

with open('C:/Users/Administrator/Documents/Projects/my-python-course/lesson22/names.txt', "w") as f:
    f.write(content)
