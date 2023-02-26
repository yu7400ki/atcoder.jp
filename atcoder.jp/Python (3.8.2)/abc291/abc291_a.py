from string import ascii_uppercase

S = input()

for i, s in enumerate(S):
    if s in ascii_uppercase:
        break

print(i + 1)
