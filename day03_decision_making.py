# challenge 1

num=int(input ("Enter a number:"))
if num<0:
   print("Negative ")
elif num>0:
   print("Positive ")
else:
   print("Zero")

# Challenge 2

num=int(input("Enter a number:"))
if num%2==0:
   print("Even")
else:
   print ("Odd")

# Challenge 3

num=int(input("Enter a number:"))
if num>=1 and num<=10:
   print("Number is between 1 and 10")
elif num>=11 and num<=20:
   print("Number is between 11 and 20")
else:
   print("Number is outside the range")

# Challenge 4

u_name= input("Enter the username:")
p_word=input("Enter the password:")
if u_name== "admin" and p_word=="1234":
   print(""Login successful "")
else:
   print(""Invalid username or password"")

# Challenge 5

age=int(input ("Enter the age:"))
if age<=12:
   print("Child")
elif age<=19:
   print("Teenager")
elif age<=59:
   print("Adult")
else:
   print ("Senior")

# Challenge 6

mark=int(input ("Enter a number:"))
if mark>=90:
   print("A Grade")
elif mark>=75:
   print("B Grade")
elif mark>=50:
   print("C Grade")
elif mark >=35:
   print ("D Grade")
else:
   print("Fail")

# Challenge 7

num1=int(input("Enter the first number:"))
num2=int(input ("Enter the second number:"))
if num1>num2:
   print("First number is greater")
elif num2>num1:
   print ("Second number is greater")
else:
   print ("Two numbers are equal")

# Challenge 8

unit=int(input("Enter the unit:"))
if unit<=100:
   print("Low usage")
elif unit<=200:
   print ("Medium usage")
elif unit<=300:
   print("High usage")
else:
   print("Very high usage")

# Challenge 9
 
year=int(input("Enter the year:"))
if year%4==0:
   print("Leap year")
else:
   print("Not a leap year")