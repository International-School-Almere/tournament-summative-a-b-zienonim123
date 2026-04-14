# main file for the Tournament App.



teams = []
individuals = []
events = []
scores = {}


def add_individual():
    name = input("Enter name of the individual: ")
    if name == "":
        print("Individual name cannot be empty.")
    else:
        individuals.append(name)
        scores[name] = 0
        print(f"Individual '{name}' added successfully.")


def add_team():
    name = input("Enter team name: ")
    if name == "":
        print("Team name cannot be empty.")
    else:
        teams.append(name)
        scores[name] = 0
        print(f"Team '{name}' added successfully.")

def add_individual_to_teams():
    individual_name = input("Enter the name of the individual to add to a team: ")
    if individual_name not in individuals:
        print(f"Individual '{individual_name}' does not exist.")
        return

    team_name = input("Enter the name of the team to add the individual to: ")
    if team_name not in teams:
        print(f"Team '{team_name}' does not exist.")
        return

    print(f"Individual '{individual_name}' added to team '{team_name}' successfully.")


def add_event():
    name = input("Enter event name: ")
    if name == "":
        print("Event name cannot be empty.")
    else:
        events.append(name)
        print(f"Event '{name}' added successfully.")


def view_scores():
    if len(scores) == 0:
        print("No scores available.")    
    else:  
        for name, score in scores.items():
            print(f"Name: {name}, Score: {score}")







def menu():
    running = True
    while running:
        print("1 - add individual")
        print("2 - add team")
        print("3 - add individual to team")
        print("4 - add event")
        print("5 - view scores")
        print("6 - exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_individual()

        elif choice == "2":
            add_team()

        elif choice == "3":
            add_individual_to_teams()
        
        elif choice == "4":
            add_event()

        elif choice == "5":
            view_scores()
        elif choice == "6":
            running = False
        else:
            print("wrong option")

menu()  