name = input("what's your name? ").strip().title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffondor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")