X = list(input())

stack = []

for x in X:
    if x == "S":
        stack.append(x)
    else:
        if stack and stack[-1] == "S":
            stack.pop()
        else:
            stack.append(x)

print(len(stack))
