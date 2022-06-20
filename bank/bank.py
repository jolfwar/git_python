def main():
    greeting = input("Enter a greeting: ")
    bank(greeting.lower())

def bank(greet):
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")

main()