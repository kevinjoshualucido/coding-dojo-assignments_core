# 1. Basic
for i in range(0, 151):
    print(i)


# 2. Multiples of Five
for j in range(5, 1_001, 5):
    print(j)


# 3. Counting, the Dojo Way
for s in range(1, 101):
    if s % 10 == 0:
        print("Coding Dojo")
    elif s % 5 == 0:
        print("Coding")
    else:
        print(s)


# 4. Whoa. That Sucker's Huge
sum = 0
for k in range(1, 500_001, 2):
    sum += k
print(sum)


# 5. Counting By Fours
for l in range(2018, 0, -4):
    print(l)


# 6. Flexible Counter
low_num = 2
high_num = 9
multiple = 3
for z in range(low_num, high_num + 1):
    if z % multiple == 0:
        print(z)
