s = input().lower()

bank = 0
for c in s:
    if ord(c) <= 122 and ord(c) >= 97:
        bank += ord(c) - 96
print(bank)
