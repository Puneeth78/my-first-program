# take the input from the user

boy_name=input("enter the boy name: " )
girl_name=input("enter the girl name: " )
print(boy_name + "  loves  " + girl_name)

# add the age diff b/w boy and girl
boy_name=input("enter the boy name: " )
boy_age=int(input("enter the boy age: "))
girl_name=input("enter the girl name: " )
girl_age=int(input("enter the girl age: "))
age_diff=boy_age-girl_age
print(boy_name + " loves " + girl_name + ".age diffrence is " + str(age_diff))
print(f"{boy_name} loves {girl_name}   .age_difference is {age_diff} ")

# # adding the abs function 
boy_name=input("enter the boy name: " )
boy_age=int(input("enter the boy age: "))
girl_name=input("enter the girl name: " )
girl_age=int(input("enter the girl age: "))
age_diff= abs (boy_age - girl_age)
print(boy_name + " loves " + girl_name + ".age diffrence is " + str(age_diff))
print(f"{boy_name} loves {girl_name}   .age_difference is {age_diff} ")

# example 1

name=input("enter the name: ")
age=int(input("enter the age:  "))
print(f" hello! {name}  you are a {age} yers old")

# ask user for two numbers and print their
print("addition",1)
print("subraction",2)
print("multiplication",3 )
print("division",4)

choice=int(input("enter your choice(1/2/3/4): "))
num1=int(input("enter the num 1:  "))
num2=int(input("enter the num 2:  "))

if choice==1:
    print("result:",num1+num2)
elif choice==2:
    print("result: ",num1-num2)
elif choice ==3:
    print("result: ",num1*num2)
elif choice==4:
    print("result: ",num1/num2)
else:
    print("enterd choice is wrong")





