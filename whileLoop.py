i = 0
while i < 10:
    print(i)
    i += 1

print()
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

print()
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    if i == 5:
        break
    i += 1
    