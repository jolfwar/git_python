def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()