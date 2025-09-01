<<<<<<< HEAD
num=int(input("enter the number: "))

fact=1
for i in range(1,num+1):
    fact*=i
print("factorial number is: ",fact)

for i in range(1,11):
    print("number: ",i,"square: ",i*i)

txt="python"
txt=txt[::-1]
for ele in txt:
    print(ele,end=" ")

num=input("enter the string: ")
vowels="aeiouAEIOU"
for ele in num:
    if ele in vowels:
        print("the vowels: ",ele)

row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

numbers = [10, 25, 7, 56, 89, 34, 67]

# Assume the first element is the largest
largest = numbers[0]

for num in numbers:
     if num > largest:
        largest = num

print("The largest number is:", largest)

student={"name":"puneeth",
         "age": 21,
         "marks":850}
for key,value in student.items():
    print(key,":", value)
=======

>>>>>>> f3170ce5f2968f22bf79e58a4d1617baace0ec01
