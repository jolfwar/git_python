def main():
    mass = int(input("Enter mass(kg): "))
    einstein(mass)

def einstein(mass):
    c = 300_000_000
    energy = mass * pow(c, 2)
    print(f"{energy:,}")


main()