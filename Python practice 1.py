#My first Python Code
name="Trishia"
age=19
GPA=5.0
#Printing type of variable
print(type(age))
print(type(GPA))

#How to input in python
name=input("What is your name: ")
print(f"Hello {name}")
age=int(input("Enter your age: "))

#Calculating area of rectangle
length=int(input("Enter length: "))
width= int(input("Enter width: "))
Area=length*width
print(f"Area= {Area}")

#Exercise: Shopping program
item=input("What item would you like to buy?--")
price=float(input("How much is it:"))
quantity=int(input("How many would you like?:"))
total= price*quantity
print(f"You may now pay {total} for your {item}")



