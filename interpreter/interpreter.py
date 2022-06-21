def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    print(calculator(x, y, z))

def calculator(x, y, z):
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)
    else: 
        print("Incorrect input.")

main()