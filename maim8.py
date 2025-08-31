# list operaton
# creating a list 

mylist=[10,20,30,40,50,60]
# print("mylist: ",mylist)

# # accessing a list element
print(mylist[2])
print(mylist[::-1])

# # updating a list
mylist[1]=25
print("after update: ",mylist)

# # addind a element
mylist.append(70)
mylist.insert(1,25)

# # removing element
mylist .pop(0)
print ( " Poped element:" ,mylist )

# # sum list
print(sum(mylist))

# # cheaking member ship
print(40 in mylist)

# counting the list by using the index
print(mylist.count(20))

# short assending order
mylist.sort()
print(mylist)

# decending order (reverse=true)
mylist.sort(reverse=True)
print(mylist)

# clesr remove all element
temp=mylist.copy()
temp.clear()
print(temp)

# list slicing
print(mylist[1:4])

# negative index
print(mylist[-1])

# conaction
list1=[1,2]
list2=[3,4]
print( list1+ list2)

# repation 
print(mylist*3)

# find length 
print(len(mylist))

# max val and min value
print("max: ",max(mylist))
print("min: ",min(mylist))


list5=["sugar","tea"]
lists=input("enter the list: ")
list.append(lists)
print(list)

list6=[1,2,3,4]
list6.append(5)
list6.insert(2,2)
list6.remove(3)
print(list6)