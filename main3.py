# FUNCTION

# simple function 
def marrage(boy,girl):
    print(f"{boy} marrage {girl}")
marrage("yash","radika")

# # function with return value
def square(num):
    return num*num
result=square(6)
print("result is : ",result)

# # function with default value

def marrage(boy,girl="kajal"):
    print(f"{boy} marrage {girl}")
marrage("puneeth")

# function with  returnng multiple value
def calc(a,b):
    return a+b,a-b,a*b
add,sub,mul=calc(10,5)
print("addition: ",add)
print("subraction:",sub)
print("multiplication: ",mul)    


def calculator(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    elif  op=="//":
        return a//b
    else:
        return "invalid operation"
print("adddition: ",calculator(10,5,"+"))
print("subraction: ",calculator(10,5,"-"))
print("multiplication: ",calculator(10,5,"*"))
print("division: ",calculator(10,5,"/"))

# factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print("factorial number is: ",factorial(5))

def sum_list(numbers):
    return sum(numbers)
numbers=[10,20,30,40]
print("total sum is: ",sum_list(numbers))

# palimdrome
def palindrome(word):
    return word == word[::-1]
print("malayalam ->",palindrome("malayalam"))
print("puneeth",palindrome("puneeth"))


def add(a,b):
    return a+b
c=add(2,3)
print(c)

# for args (tuples)
def add(*numbers):
    return sum(numbers)
print(add(1,2,3))

# kwargs for(dict)
def student_info(**details):
    print(type(details))
    for key, value in details.items():
        print({f"{key} : {value}"})

student_info(name="puneeth",age=22,course="python")

# add lambda function
add=lambda a,b : a+b
print(add(5,5))

double=lambda x : 2*x
print(double(200))

# recursion argument
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
num=int(input("enter the number: "))
print("factorial number is : ",factorial(num))



    