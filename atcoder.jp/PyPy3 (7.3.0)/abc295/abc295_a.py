N = int(input())
W = input().split()

W = set(W)

if W & set(["and", "not", "that", "the", "you"]):
    print("Yes")
else:
    print("No")
