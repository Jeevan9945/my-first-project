print("Hello world")
print("jeevan")
print("Vikas K A")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

while True:
    a = input("Enter the Operator(+,-,*,/): ")

    if a in ['+','-','*','/']:
        if a == "+":
            z = x + y
        elif a == "-":
            z = x - y
        elif a == "*":
            z = x * y
        else:
            z = x / y

        print("Result:", z)
        break
    else:
        print("Operator is not correct")