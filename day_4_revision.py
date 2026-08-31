# Challenge 1

num=int(input("Enter a number:"))
if num>0:
   print("Positive")
elif num==0:
   print("Zero")
else:
   print("Negative")

# Challenge 2

name=input("Enter the name:")
mark=int(input ("Enter the mark:"))
if mark>=35:
   print(name,"-Pass")
else:
   print (name,"-Fail")

# Challenge 3

age=int(input ("Enter a number:"))
att_per=int(input ("Enter a Attendance percentage:"))
if age>=18 and att_per>=75:
   print ("Eligible")
else:
   print (" Not eligible ")
day=input("Enter a day:")

# Challenge 4
if day=="Sunday" or day=="Saturday":
   print("It's a weekend!")
else:
   print(" It's a weekday!")

# Challenge 5

mark= int(input("Enter the mark:"))
if mark>=90:
   print("A")
elif mark>=75:
   print ("B")
elif mark>=50:
   print("C")
elif mark>=35:
   print("D")
else:
   print ("Fail")
