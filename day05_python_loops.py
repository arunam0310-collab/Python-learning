# Challenge 1

for i in range (1, 11) :
   print(i)

# Challenge 2

for i in range(2, 21, 2):
    print(i)

# Challenge 3

num = int(input("Enter a number:"))
i = 1

while i <= 10:
    mul = num * i
    print(num, "*", i, "=", mul)
    i = i + 1

# Challenge 4

i = 10

while i >= 1:
    print(i)
    i = i - 1

# Challenge 5

num = int(input("Enter a number:"))
total = 0

for i in range(1, num + 1):
    total = total + i

print("Sum =", total)