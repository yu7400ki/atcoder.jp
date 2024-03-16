import re

S = input()

if re.match(r"^<=+>$", S):
    print("Yes")
else:
    print("No")
