1. Creating and Printing a List

fruits = ["apple", "banana", "cherry"]
print(fruits)

🔹 2. Accessing Elements

numbers = [10, 20, 30, 40]
print(numbers[0])   # first element
print(numbers[-1])  # last element

 3. Adding Elements
animals = ["dog", "cat"]
animals.append("elephant")     # add at end
animals.insert(1, "tiger")     # add at position
print(animals)



🔹 4. Removing Elements
colors = ["red", "blue", "green", "yellow"]
colors.remove("green")     # remove by value
colors.pop(1)              # remove by index
print(colors)


🔹 5. Updating Elements
marks = [45, 67, 89, 76]
marks[2] = 95
print(marks)

🔹 6. Iterating (Looping through a List)
names = ["Asha", "Ravi", "Kiran"]
for name in names:
    print(name)


🔹 7. List Slicing
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:4])   # from index 1 to 3
print(letters[:3])    # from start to index 2
print(letters[2:])    # from index 2 to end


🔹 8. List Comprehension

👉 Create new lists using one line.

squares = [x*x for x in range(6)]
print(squares)


🔹 9. Sorting a List
nums = [4, 1, 7, 3]
nums.sort()
print(nums)



🔹 10. Nested Lists (List inside a List)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])   # row 2, column 3


🔹 11. Length of List
items = ["pen", "book", "pencil"]
print(len(items))


🔹 12. Checking Membership
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)
print("grape" not in fruits)

