# main file for the Tournament App.

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

teams = []
individuals = []
events = []
scores = {}
teammembers = {}
eventparticipants = {}
eventresults = []


def save_data():
    data = {
        "teams": teams,
        "individuals": individuals,
        "events": events,
        "scores": scores,
        "teammembers": teammembers,
        "eventparticipants": eventparticipants,
        "eventresults": eventresults
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    global teams, individuals, events, scores, teammembers, eventparticipants, eventresults

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            teams = data.get("teams", [])
            individuals = data.get("individuals", [])
            events = data.get("events", [])
            scores = data.get("scores", {})
            teammembers = data.get("teammembers", {})
            eventparticipants = data.get("eventparticipants", {})
            eventresults = data.get("eventresults", [])
    except (FileNotFoundError, json.JSONDecodeError):
        pass


def add_individual():
    name = simpledialog.askstring("Add Individual", "Enter name of the individual:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Individual name cannot be empty.")
    elif name in individuals:
        messagebox.showerror("Error", "This individual already exists.")
    else:
        individuals.append(name)
        scores[name] = 0
        save_data()
        messagebox.showinfo("Success", f"Individual '{name}' added successfully.")


def add_team():
    name = simpledialog.askstring("Add Team", "Enter team name:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Team name cannot be empty.")
    elif name in teams:
        messagebox.showerror("Error", "This team already exists.")
    else:
        teams.append(name)
        teammembers[name] = []
        scores[name] = 0
        save_data()
        messagebox.showinfo("Success", f"Team '{name}' added successfully.")


def add_individual_to_teams():
    individual_name = simpledialog.askstring("Add Individual to Team", "Enter individual name:")
    if individual_name is None:
        return
    individual_name = individual_name.strip()

    if individual_name not in individuals:
        messagebox.showerror("Error", "Individual does not exist.")
        return

    team_name = simpledialog.askstring("Add Individual to Team", "Enter team name:")
    if team_name is None:
        return
    team_name = team_name.strip()

    if team_name not in teams:
        messagebox.showerror("Error", "Team does not exist.")
        return

    if individual_name in teammembers[team_name]:
        messagebox.showerror("Error", "This individual is already in this team.")
    else:
        teammembers[team_name].append(individual_name)
        save_data()
        messagebox.showinfo("Success", f"Added {individual_name} to {team_name}")


def add_event():
    name = simpledialog.askstring("Add Event", "Enter event name:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Event name cannot be empty.")
    elif name in events:
        messagebox.showerror("Error", "This event already exists.")
    else:
        events.append(name)
        eventparticipants[name] = []
        save_data()
        messagebox.showinfo("Success", f"Event '{name}' added successfully.")


def add_participant_to_event():
    event_name = simpledialog.askstring("Add to Event", "Enter event name:")
    if event_name is None:
        return
    event_name = event_name.strip()

    if event_name not in events:
        messagebox.showerror("Error", "Event does not exist.")
        return

    participant_name = simpledialog.askstring("Add to Event", "Enter individual or team name:")
    if participant_name is None:
        return
    participant_name = participant_name.strip()

    if participant_name not in individuals and participant_name not in teams:
        messagebox.showerror("Error", "Participant does not exist.")
        return

    eventparticipants.setdefault(event_name, [])

    if participant_name in eventparticipants[event_name]:
        messagebox.showerror("Error", "Participant is already added to this event.")
    else:
        eventparticipants[event_name].append(participant_name)
        save_data()
        messagebox.showinfo("Success", f"Added {participant_name} to event {event_name}")


def add_team_to_event():
    event_name = simpledialog.askstring("Add Team to Event", "Enter event name:")
    if event_name is None:
        return
    event_name = event_name.strip()

    if event_name not in events:
        messagebox.showerror("Error", "Event does not exist.")
        return

    team_name = simpledialog.askstring("Add Team to Event", "Enter team name:")
    if team_name is None:
        return
    team_name = team_name.strip()

    if team_name not in teams:
        messagebox.showerror("Error", "Team does not exist.")
        return

    eventparticipants.setdefault(event_name, [])

    if team_name in eventparticipants[event_name]:
        messagebox.showerror("Error", "Team is already added to this event.")
    else:
        eventparticipants[event_name].append(team_name)
        save_data()
        messagebox.showinfo("Success", f"Added team {team_name} to event {event_name}")


def calculate_points(position):
    if position == 1:
        return 10
    elif position == 2:
        return 8
    elif position == 3:
        return 6
    elif position == 4:
        return 4
    else:
        return 0


def add_score():
    event_name = simpledialog.askstring("Add Score", "Enter event name:")
    if event_name is None:
        return
    event_name = event_name.strip()

    if event_name not in events:
        messagebox.showerror("Error", "Event does not exist.")
        return

    participant_name = simpledialog.askstring("Add Score", "Enter individual or team name:")
    if participant_name is None:
        return
    participant_name = participant_name.strip()

    if participant_name not in scores:
        messagebox.showerror("Error", "Participant or team does not exist.")
        return

    position_text = simpledialog.askstring("Add Score", "Enter rank position:")
    if position_text is None:
        return

    try:
        position = int(position_text)
    except ValueError:
        messagebox.showerror("Error", "Position must be a number.")
        return

    points = calculate_points(position)
    scores[participant_name] += points

    eventresults.append({
        "event": event_name,
        "participant": participant_name,
        "position": position,
        "points": points
    })

    save_data()
    messagebox.showinfo("Success", f"Added {points} points to {participant_name}.")


def view_scores():
    if len(eventresults) == 0:
        messagebox.showinfo("Scores", "No event results available.")
    else:
        text = "Event results:\n\n"

        for result in eventresults:
            text += f"{result['event']} - {result['participant']} - position {result['position']} - {result['points']} points\n"

        messagebox.showinfo("Scores", text)


def view_leaderboard():
    if len(scores) == 0:
        messagebox.showinfo("Leaderboard", "No scores available.")
    else:
        text = "Leaderboard:\n\n"
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        for name, score in sorted_scores:
            text += f"{name}: {score} points\n"

        messagebox.showinfo("Leaderboard", text)


def view_event_participants():
    if len(eventparticipants) == 0:
        messagebox.showinfo("Event Participants", "No event participants available.")
    else:
        text = "Event participants:\n\n"

        for event_name, participants in eventparticipants.items():
            text += f"{event_name}: "
            if len(participants) == 0:
                text += "No participants\n"
            else:
                text += ", ".join(participants) + "\n"

        messagebox.showinfo("Event Participants", text)


load_data()

root = tk.Tk()
root.title("Tournament App")
root.geometry("400x500")

label = tk.Label(root, text="Tournament App", font=("Arial", 16))
label.pack(pady=10)

tk.Button(root, text="Add Individual", command=add_individual).pack(pady=5)
tk.Button(root, text="Add Team", command=add_team).pack(pady=5)
tk.Button(root, text="Add Individual to Team", command=add_individual_to_teams).pack(pady=5)
tk.Button(root, text="Add Event", command=add_event).pack(pady=5)
tk.Button(root, text="Add Participant to Event", command=add_participant_to_event).pack(pady=5)
tk.Button(root, text="Add Team to Event", command=add_team_to_event).pack(pady=5)
tk.Button(root, text="Add Score", command=add_score).pack(pady=5)
tk.Button(root, text="View Scores", command=view_scores).pack(pady=5)
tk.Button(root, text="View Leaderboard", command=view_leaderboard).pack(pady=5)
tk.Button(root, text="View Event Participants", command=view_event_participants).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
