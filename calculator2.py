def main():
    x = float(input("What's x? "))
    print(f"x squared is {square(x):.2f}")
    print(f"x cubed is {cube(x):.2f}")

def square(n):
    return pow(n, 2)

def cube(n):
    return pow(n, 3)

main()