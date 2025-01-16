name = "Dave"
count = 1

def another():
    global count
    count = 2
    print(count)
    def greeting(firstname):
        color = "blue"
        print(color)
        print(name)
        print(firstname)
    greeting("Dave")
    greeting("John")

another()
print(count)
