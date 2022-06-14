# Ask user for their name
name = input("What's your name? ").strip().title()
planet = input("What planet are you located on? ").strip().title()

# Say hello to user
print(f"Hello, {name}. ", end='')
print(f"You're located on planet {planet}.")