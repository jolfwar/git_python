def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")

    if time.endswith("a.m."):
        minutes = minutes.rstrip(" a.m.")
        if int(hours) >= 7 and int(hours) <= 8:
            print("Breakfast Time!")
        else:
            print("No food allowed!")
    elif time.endswith("p.m."):
        minutes = minutes.rstrip(" p.m.")
        if int(hours) == 12 or (int(hours) == 1):
            print("Lunch Time!")
        elif int(hours) >= 6 and (int(hours) <= 7):
            print("Dinner Time!")
        else:
            print("No food allowed!")
    else:
        if int(hours) < 24 and int(minutes) < 60:
            if int(hours) >= 7 and int(hours) < 8:
                print("Breakfast Time!")
            elif int(hours) >= 12 and int(hours) < 13:
                print("Lunch Time!")
            elif int(hours) >= 18 and int(hours) < 19:
                print("Dinner Time!")
            else:
                print("No food allowed!")
        else:
            print("You exceeded a standard day!")


main()