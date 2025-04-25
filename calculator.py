num1 = float(input("Enter the First number: "))
operation = input("choose an operation (+,-,*,/): ")
num2 = float(input("Enter the Second number: "))

# Perform the operation

if operation == "+" :
    result = num1+num2
elif operation == "-" :
    result = num1-num2
elif operation == "*" :
    result = num1*num2
elif operation == "/" :
    if num2 != 0:
        result = num1/num2
    else:
         result = "Error! Division by Zero."
else:
    result = "Invalid operation!"

print("result: " , result)









