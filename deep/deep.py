def main():
    deep = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    deep_thought(deep)

def deep_thought(thought):

    if  thought == "forty-two" or thought == "forty two" or thought == "42":
        print("Yes")
    else:
        print("No")

main()