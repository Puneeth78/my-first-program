i=1
while i<=10:
    print(i)
    i+=1

i=1
while i<=50:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=50:
    if i%2==0:
        i+=1
        continue
    i+=1
    print(i)

i=1
total=0
while i<=10:
    total+=i
    i+=1
print("total",total)

num=int(input("enter the  number: "))
while num>=1:
    print(num)
    num=num-1

n=int(input("enter the number: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print("factorial numn: ",fact)


num=int(input("enter the num: "))
i=1
while i<=10:
    print(num*i)
    i+=1
    continue

num=int(input("enter the number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("reversed number is: ",reverse)


n=int(input("enter the number: "))
count=0
while n>0:
    n=n//10
    count+=1
print("total digit: ",count)

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
