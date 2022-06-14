# Ask user for their name
name = input("What's your name? ")
planet = input("What planet are you located on? ")

# Removes whitespace from strings
name, planet = name.strip(), planet.strip()

# Capitalize strings from user input
name, planet = name.upper(), planet.upper()

# Say hello to user
print(f"Hello, {name}. ", end='')
print(f"You're located on planet {planet}.")