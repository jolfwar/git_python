def main():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    numOperator = int(input("Enter the corresponding number associated with an operator:"))
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if numOperator == 1:
        calcAdd(num1, num2)
        print(f"\n{num1:,} + {num2:,} is {calcAdd(num1, num2):,}!")

    elif numOperator == 2:
        calcSubtract(num1, num2)

    elif numOperator == 3:
        calcMultiply(num1, num2)
    
    elif numOperator == 4:
        calcDivide(num1, num2)
    
    else:
        print("Error. Invalid input. Please enter a number 1 - 4.")

def calcAdd(x, y):
    return x + y

def calcSubtract(x, y):
    print (x - y)

def calcMultiply(x, y):
    print (x * y)

def calcDivide(x, y):
    print (x / y)

main()