operation= str(input("Choose an operation(+,-,*,/):"))
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

if operation=='+':
    print("Addition")
    result=n1+n2
    print(f"{n1}+{n2}={result}")
elif operation =='-':
    print("Subtraction")
    result=n1-n2
    print(f"{n1}-{n2}={result}")
elif operation=='*':
    print("Multiplication")
    result=n1*n2
    print(f"{n1}*{n2}={result}")
elif operation=='/':
    if n2==0:
        print("Math error")
    else:
        print("Division")
        result=n1/n2
        print(f"{n1}/{n2}={result}")
else:
    print("Syntax error")
        