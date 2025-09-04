# *) examples for while loop 

# 1) Write a Python program to print numbers from 1 to 10 using a while loop.

i=1
while i<=10:
    print(i)
    i+=1

 # 2) Write a Python program to print all odd numbers from 1 to 50 using a while loop.
i=1
while i<=50:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1

# Write a Python program to print all odd numbers +1 (next number after odd) from 1 to 50 using a while loop.
i=1
while i<=50:
    if i%2==0:
        i+=1
        continue
    i+=1
    print(i)

# Write a Python program to find the sum of first 10 natural numbers using a while loop.
i=1
total=0
while i<=10:
    total+=i
    i+=1
print("total",total)


# Write a Python program to print numbers in reverse order starting from a given number.
num=int(input("enter the  number: "))
while num>=1:
    print(num)
    num=num-1

# Write a Python program to find the factorial of a number using a while loop.
n=int(input("enter the number: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print("factorial numn: ",fact)

# Write a Python program to print the multiplication table of a given number using a while loop.
num=int(input("enter the num: "))
i=1
while i<=10:
    print(num*i)
    i+=1
    continue

# Write a Python program to reverse a number using a while loop.
num=int(input("enter the number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("reversed number is: ",reverse)

# Write a Python program to count the number of digits in a given number using a while loop.
n=int(input("enter the number: "))
count=0
while n>0:
    n=n//10
    count+=1
print("total digit: ",count)

# Write a Python program to check whether a number is a palindrome or not using a while loop.
n=int(input("enter the number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("palindrome ")
else:
    print("not palindrome")
