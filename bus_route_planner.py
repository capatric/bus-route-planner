import tkinter as tk
from tkinter import ttk
import os

APP_TITLE = "GDL Bus Route Planner"
WINDOW_SIZE = "400x300"
RESULTS_WINDOW_SIZE = "400x350"
ICON_FILE = "bus.png"
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_SUBTITLE = ("Helvetica", 14)
FONT_LABEL = ("Helvetica", 12)

def main_window():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(WINDOW_SIZE)
    set_icon(root)
    return root

# Set window icon
def set_icon(window):
    logo_path = os.path.join(os.path.dirname(__file__), ICON_FILE)
    logo = tk.PhotoImage(file=logo_path)
    window.iconphoto(False, logo)

# Create and pack a label
def create_label(parent, text, font, pady=(0, 0)):
    label = tk.Label(parent, text=text, font=font)
    label.pack(pady=pady)
    return label

# Create and pack an entry
def create_entry(parent, width=25, pady=5):
    entry = tk.Entry(parent, width=width)
    entry.pack(pady=pady)
    return entry

# Create results window
def results_window(route_tuple):
    new_window = tk.Toplevel(root)
    new_window.title(APP_TITLE)
    new_window.geometry(RESULTS_WINDOW_SIZE)
    set_icon(new_window)
    create_label(new_window, "This is the best route", FONT_SUBTITLE, pady=20)
    create_scrollable_frame(new_window, route_tuple)

# Create a scrollable frame
def create_scrollable_frame(parent, route_tuple):
    canvas = tk.Canvas(parent)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for location in route_tuple:
        create_location_frame(scrollable_frame, location)

# Create a frame for each location
def create_location_frame(parent, location):
    location_frame = tk.Frame(parent)
    location_frame.pack(fill='x', pady=5)
    
    icon_label = tk.Label(location_frame, text="►", font=FONT_LABEL)
    icon_label.pack(side='left', padx=80)
    
    location_label = tk.Label(location_frame, text=location, font=FONT_LABEL)
    location_label.pack(side='left')

# Plan route
def plan_route():
    # Get Inputs
    from_location = from_entry.get()
    to_location = to_entry.get()
    
    # Process Route
    print(f"Planning route from {from_location} to {to_location}")
    
    # Show results
    route_tuple = ("Guadalajara", "Queretaro", "CDMX", "Puebla", "Monterrey", "Tijuana", "Cancun", "Merida", "Leon", "Toluca")
    results_window(route_tuple)

# Main application
root = main_window()
create_label(root, "Guadalajara", FONT_TITLE, pady=(10, 0))
create_label(root, "Bus Route Planner", FONT_SUBTITLE, pady=(0, 10))
create_label(root, "FROM:", FONT_LABEL)
from_entry = create_entry(root)
create_label(root, "TO:", FONT_LABEL)
to_entry = create_entry(root)
enter_button = tk.Button(root, text="Enter", command=plan_route, width=15, height=2)
enter_button.pack(pady=20)

if __name__ == "__main__":
    root.mainloop()
