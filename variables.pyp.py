name= input("What is your name: ")
print(name)
#Comments out a single line

a=2
b=10
multiply=a*b
print(multiply)
#if loops
mark=20
if mark>20:
    print("You have passed")
elif mark==20:
    print("You are kawa")
else:
    print("Failed")
#while loops
number=0
while number<10:
    print(f"Number is:{number}")
    number +=1
#functions
length=20
width=12
def calculate_area(length,width):#def is wat defines a function
    return length*width
print("Area is ",calculate_area(length,width))
