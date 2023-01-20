def madlib():
    slur = input("Slur: ")
    creature = input("Creature: ")
    item = input("Item: ")
    while item[0] == "a":
        print("Pls don't use the letter 'a' or 'an' in the beginning")
    item = input("Item: ")
    adj = input("Adjective: ")

    madlib = (f"Oh {slur}, watch out there's a {creature} over there! U better \
    use the {item} to kill it. I really do hope it works...Oh wow, that just made it {adj}")
    print(madlib)