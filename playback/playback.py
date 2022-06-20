def main():
    word = input("Enter a phrase: ")
    print(playback(word))

def playback(a):
    a = a.replace(" ", "...")
    return (a)



main()