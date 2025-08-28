#examples of variables and datatypes

x="puneeth"
print(type(x),x)

y=123
print(type(y),y)

z=True
print(type(z),y)

a=1.5
print(type(a),a)


# type conversion 

b="10" # this is string
c=int(b) # this is a integer
d=float(c) # this is a float
print(type(b),b)
print(type(c),c)
print(type(d),d)

# data types
# numaric data types
x=1,2,3  #integer data type
print(x)  # out put = 1,2,3

p=10.5   #float datatypes
print(p) #out put = 10.5

g=True #boolean data type
print(g) #ouut put =True

# complex data types
a=2+5j  #2 is real and 5j is a imaginary
print(type(a),a) # out put= complex,2+5j

# sequence data types

# list , tuples, dictnory
list=[1,2,3,"puneeth"]
print(list)

# # tuples
tuples=(1,2,3)
print(tuples)

# # dictonary
dict={"puneeth":2,"manjunath":3,"sudeep":3}
print(dict)


# assining the value into multiple variables
a,b,c=10,20,30
print(a) 
print(b)
print(c)