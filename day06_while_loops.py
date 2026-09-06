# Challenge 1

i = 1
while i <= 10:
    print(i)
    i = i + 1

# Challenge 2

num = int(input("Enter a number:"))
i = 1

while i <= 10:
    mul = num * i
    print(num, "×", i, "=", mul)
    i = i + 1

# Challenge 3

num = int(input("Enter a number:"))
i = 1
sum = 0

while i <= num:
    sum = sum + i
    i = i + 1

print("Sum =", sum)

# Challenge 4

num = int(input("Enter a number:"))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)

# Challenge 5

num = int(input("Enter a number:"))
count = 0

while num > 0:
    count = count + 1
    num = num // 10

print("Number of digits =", count)