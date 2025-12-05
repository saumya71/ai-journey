a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
op = input("Enter Operator(+ - * /)")

if op== "+":
    print("Result: ", a+b)
elif op== "-":
    print("Result: ", a-b)
elif op== "*":
    print("Result: ", a*b)
elif op== "/":
    if b==0:
        print("Division by 0 Not Possible!")
    else:
        print("Result: ", a/b)
else:
    print("Invalid Operation")