# Stack using functions

stack = []

def push(item):
    stack.append(item)
    print(item, "pushed")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped")

push(100)
push(200)
push(300)

print("Stack:", stack)

pop()
print("Stack after pop:", stack)
