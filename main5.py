# string manupulation

# 1) commom string operatiomn

# first_name=input("enter the first name: ")
# last_name=input("enter the last name:  ")
# full_name=first_name + " " + last_name
# print(full_name)

#  repetition
# message= " puneeth "
# print(message * 10)

# comman string methods in python

# 1) upper() converted into upper case
# text="hello, world"
# print(text.upper())  #op HELLO WORLD
# print(text.lower()) # op hello world
# print(text.title())  #op Hello World
# print(text.capitalize()) # Hello world
# print(text.strip()) # hello world
# print(text.replace("world","puni")) # hello puni
# print("-".join("hello world"))
# print(text.find("wo"))
# print(text.count("l"))
# print(text.split(","))


# accessing the chareacter
name="puneeth"
print(name[0])
print(name[2])
print(name[-1]) # negattive value
print(name[-2])  # negattive value

# string sliceing

text="davangere"
print(text[0:5])
print(text[:3])
print(text[3:])
print(text[:-3])
print(text[::-1]) #reversing
print(text[::2])