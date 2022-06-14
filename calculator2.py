# Displays and formats result of square and cube functions
def main():
    x = float(input("What's x? "))
    print(f"x squared is {square(x):.2f}")
    print(f"x cubed is {cube(x):.2f}")

# Squares the user input (x)
def square(n):
    return pow(n, 2)

# Cubes the user input (x)
def cube(n):
    return pow(n, 3)

main()