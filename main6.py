
# string creation and basic operation
# 1) string concatination
text="python"
b="programing"
print(text + " " + b)
print(f"{text}  {b}")

# 2) string repeation
print(text * 5)

#   sring indexing and sliding
# 3) string indexing
print(text[0])
print(text[-1])

# string slicing
print(text[0:6])
print(text[0:5])

# string cheaking
print("python".endswith("on"))
print("python".startswith("on"))

# string content
print("123".isdigit())
print("pun".isalpha())
print("pun123".isalnum())

# find a substring
# find sub string

text="python is fun"
print(text.find("fun"))

# count occarunce
name="puneeth"
print(name.count("e"))


# string replacement  and spliting
# string split
text="apple,banana,orange"
print(text.split(","))

# string replace and spliting
text="puneeth like yash"
print(text.replace("yash", "thalapathy vijay"))

# join string
text=["python","is","cool"]
print(" ".join(text))


# removing extra space  using strip
text="  hello   "
print(text.strip())

# formated string take input from the user
name=input("enter the name: ")
age=int(input("enter the age: "))
print(f"my name is {name} and iam {age} year old ")

# reversing a string
text="puneeth"
print(text[::-1])

