# main file for the Tournament App.

teams = []
individuals = []
events = []
scores = {}


def menu():
    running = True
    while running:
        print("1 - add individual to the teams")
        print("2 - add team")
        print("3 - add event")
        print("4 - view scores")
        choice = input("Choose option: ")

        if choice == "1":
            print("add individual to the teams")

        elif choice == "2":
            add_team()

        elif choice == "3":
            add_event()
        
        elif choice == "4":
            view_scores()
        else:
            print("wrong option")

menu()  