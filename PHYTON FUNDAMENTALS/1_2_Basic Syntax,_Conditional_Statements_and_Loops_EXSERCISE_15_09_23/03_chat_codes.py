messages_number = int(input())

for message in range(messages_number):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number > 88:
        print("Bye.")
    else:
        print("GREAT!")