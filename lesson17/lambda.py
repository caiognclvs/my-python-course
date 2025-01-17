from functools import reduce

def squared(num): return num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(3))

sumtwo = lambda a, b: a + b

print(sumtwo(2, 2))

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

numbers = [2, 3, 543, 123, 1, 12]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

print(sum(numbers))

names = ["Dave Gray", "Sara Ito", "John Jacob Jinglehwimerschmidt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
