# main file for the Tournament App.

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

teams = []
individuals = []
events = []
scores = {}
teammembers = {}


def add_individual():
    name = simpledialog.askstring("Add Individual", "Enter name of the individual:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Individual name cannot be empty.")
    else:
        individuals.append(name)
        scores[name] = 0
        messagebox.showinfo("Success", f"Individual '{name}' added successfully.")


def add_team():
    name = simpledialog.askstring("Add Team", "Enter team name:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Team name cannot be empty.")
    else:
        teams.append(name)
        teammembers[name] = []
        scores[name] = 0
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

    teammembers[team_name].append(individual_name)
    messagebox.showinfo("Success", f"Added {individual_name} to {team_name}")


def add_event():
    name = simpledialog.askstring("Add Event", "Enter event name:")
    if name is None:
        return
    name = name.strip()

    if name == "":
        messagebox.showerror("Error", "Event name cannot be empty.")
    else:
        events.append(name)
        messagebox.showinfo("Success", f"Event '{name}' added successfully.")


def view_scores():
    if len(scores) == 0:
        messagebox.showinfo("Scores", "No scores available.")
    else:
        text = ""
        for name, score in scores.items():
            text += f"{name}: {score}\n"
        messagebox.showinfo("Scores", text)


# GUI
root = tk.Tk()
root.title("Tournament App")
root.geometry("400x350")

label = tk.Label(root, text="Tournament App", font=("Arial", 16))
label.pack(pady=10)


tk.Button(root, text="Add Individual", command=add_individual).pack(pady=5)
tk.Button(root, text="Add Team", command=add_team).pack(pady=5)
tk.Button(root, text="Add Individual to Team", command=add_individual_to_teams).pack(pady=5)
tk.Button(root, text="Add Event", command=add_event).pack(pady=5)
tk.Button(root, text="View Scores", command=view_scores).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)


root.mainloop()
