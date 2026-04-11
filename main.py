# main file for the Tournament App.

teams = []
individuals = []
events = []
scores = {}


def menu():
    running = True
    while running:
        choice = input("Choose option: ")

        if choice == "1":
            print("add individual to the teams")
        elif choice == "2":
            print("second option")
        
        elif choice == "3":
            print("second option")
        else:
            print("wrong option")