def main():
    fileType = input("File Name: ")
    file(fileType.lower())

def file(fileType):
    if fileType.endswith(".gif"):
        print("image/gif")
    elif fileType.endswith(".jpg"):
        print("image/jpg")
    elif fileType.endswith(".jpeg"):
        print("image/jpeg")
    elif fileType.endswith(".png"):
        print("image/png")
    elif fileType.endswith(".pdf"):
        print("application/pdf")
    elif fileType.endswith(".txt"):
        print("text/plain")
    elif fileType.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()