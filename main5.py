#  simple python examples

text=input("enter the string : ")
count=0
i=0
while i<=len(text):
    count+=1
    i+=1
print("length of sting is : ",count)


# cal the sq using math
# import math
input=int(input("enter the num: "))
ch=math.sqrt(input)
print("number is : ",ch)

#  area of triangle
num1=int(input("enter the height of triangle: "))
num2=int(input("enter the base of triangle: "))
area = (1/2)*num2*num2
print("areaz of triangle is: ",area)

# swapping of two numbers
a=10
b=20
a,b=b,a
print(a,b )

# kilometer into miles
num=int(input("enter the kilometer: "))
miles=num*0.621371
print("in miles is : ",miles)

#  cheak the number positive negartive or zero
number=int(input("enter the number: "))
if number>0:
    print("positive",number)
elif number == 0:
    print("equal to zero")
else:
    print("neagtive")

# print the number is even or odd
nums=int(input("enter the number: "))
if nums % 2 == 0:
    print("even",nums)
else:
    print("odd",nums)

#  cheak the leap year or not
year=int(input("enter the year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("leap year",year)
elif (year % 4 == 0) and (year % 100 !=0):
    print("not a leap year",year)

# find the largest number
num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
if num1>num2 :
    print("print num 1 is greather: ",num1)
else:
    print("num 2 is greather ",num2)

# palindrome 
name=input("enter the string: ")
if name==name[::-1]:
    print("string is palindrome: ",name)
else:
    print("string  is not palindrome : ",name)

# remove all the vowels
names=input("enter the string: ")
vowels="aeiouAEIOU"
result="" 
for i in names:
    if i not in  vowels:
        result+=i
print("string without vowels: ",result)

# cheak the num is prime or not
num=int(input("enter the number: "))
if num==1:
   print("it is not a prime number")
if num>1:
 for i in range(2,num):
    if num % i == 0:
     print("num is not prime",num)
    break
else:
        print("num is a prime",num)


# num is a prime number
num =int(input("enter the number: "))
if num==1:
    print("num is not prime")
elif num > 1:
    print("num is prime")
    for i in range (2,num):
        if num % i==0:
            print("not prime")
    else:
        print("prime")

# python program to generate random number
import random
num=random.randint(0,10)
print(num)

# to print all prime numbers
lower=int(input("enter the lower: "))
upper=int(input(" enter the upper: "))
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if num % i==0:
                break
        else:
            print(num)

# convert degree to fahrenheit
celsius=int(input("enter the celsius: "))
fahreheit=(celsius*(9/5))+32
print("converted fahrenheit is  ",fahreheit)






