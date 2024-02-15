import re

S = input()

is_capitalized = re.match(r"^[A-Z][a-z]*$", S)

if is_capitalized:
    print("Yes")
else:
    print("No")
