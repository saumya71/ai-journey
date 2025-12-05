temp = float(input("Enter Temperature: "))
mode = input("Enter Conversion (CtoF or FtoC): ")

if mode == "CtoF":
    f = (temp*(9/5))+32
    print("Temperature in Farenheit: ",f)
elif mode == "FtoC":
    c = (temp-32)*(5/9)
    print("Temperature in Celcius: ",c)
else:
    print("Invalid mode")