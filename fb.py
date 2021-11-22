def fb(n):
    return [
        'FizzBuzz'[(i % -3) & -4: i % -5 & 8 ^ 12] or str(i)
        for i in range(1, n + 1)
    ]

print(fb(20))

for i in range(1, 21):
    print(i, i % -3, i % -3 & -4)