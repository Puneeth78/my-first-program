
# examples for loop


year=int(input("enter the year: "))
if year%400==0 or year%4==0:
    print("leap year: ",year)
else:
    print("year is not a leep year",year)

# print numbers 1 to 10
for i in range(1,11):
    print(i)

# print even numbers between 1 to 20
for i in range(2,20,2):
    print(i)

# print odd numbers  from 1 to 20
for num in range(1,21,2):
    print(num)

# multliplication of tables
number=int(input("enter the number: "))
for i in range(1,11):
    print(f"{number}*{i}={number*i}")

# sum of first n numbers
n=int(input("enter the number: "))
total=0
for i in range(1,n+1):
    total+=i
print("sum=",total)

# factorial number
num=int(input("enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial num is : ",fact)

txt=input("enter the string: ")
for ch in txt:
    print(ch)

# find the vowels in a string
text=input("enter a text: ")
count=0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
print("vowels is  : ",count)

# reverse the string
txt=input("enter the string: ")
rev=""
for ch in txt:
    rev=ch+rev
print("reversed=",rev)

# find the max element in a list
nums=[1,2,3,4,5]
max_val=nums[0]
for n in nums: 
    if n > max_val:
        max_val=n
print("maximum=",max_val)
