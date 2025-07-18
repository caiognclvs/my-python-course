users = ["Dave", "John", "Sarah"]

data = ["Dave", 33, True]

empty = []

print("Dave" in users)

print(users[0])
print(users[-2])
print(users[0])

print(users.index("Sarah"))

print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 35, 423, 5324]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print("")

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

mytuple = tuple(("Dave", 23, True))

anotherTuple = (1, 43, 643, 213)

print(mytuple)
print(type(mytuple))
print(type(anotherTuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count())
