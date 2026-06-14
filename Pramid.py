# Star Pyramid patterns
for i in range(1, 6):
    for space in range(1, 6-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()