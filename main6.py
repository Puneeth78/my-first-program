# # def recursive_parameters(parameters):
# if base_condition:
#     return result
# else:
#     return recursive_function(smaller_problem)

# factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial num:",factorial(5))

# #  sum first n numbers
def sum_n(n):
    if n==0:
        return 0
    else:
        return n+sum_n(n-1)
print(sum_n(5))

# # finbonacci 
n=int(input("enter the number: "))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(n):
  print(f"fibonacci({i})={fibonacci(i)}")

# print num 1 to n
def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)
print(print_1_to_n(5))

# # power of n
def power_n(x,n):
    if n==0:
        return 1
    else:
        return x*power_n(x,n-1)
print(power_n(2,2))

#  print n to 1
def print_n_to_1(n):
    if n==0:
        return
    print(n)
    print_n_to_1(n-1)
print_n_to_1(5)

# reverse string
def reverse_string(s):
    if len(s)==0:
        return ""
    else:
        return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))

#  count digits
def count_digits(n):
    if n==0:
        return 0
    else:
        return 1 + count_digits(n//10)
print(count_digits(123456))

#  greatest element in a list
def max_list(list,num):
    if num==0:
        return list[0]
    else:
        return max(list[num-1],max_list(list,num-1))
print(max_list([1,2,3,4,5,63],6))

# decimal to binary
def dec_to_bin(n):
    if n == 0:                # base case
        return ""
    return dec_to_bin(n // 2) + str(n % 2)

print(dec_to_bin(10))   # "1010"
    







