import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def get_selected_datetime():
    selected_datetime_str = calendar_entry.get()
    try:
        selected_datetime = datetime.strptime(selected_datetime_str, "%Y-%m-%dT%H:%M")
        messagebox.showinfo("Selected Date Time", f"You selected: {selected_datetime}")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter date in YYYY-MM-DDTHH:MM format.")

# Create main window
root = tk.Tk()
root.title("Date Time Selection")

# Create a label
label = ttk.Label(root, text="Call Date Time")
label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Create an Entry widget for date-time input
calendar_entry = ttk.Entry(root)
calendar_entry.grid(row=0, column=1, padx=10, pady=5)

# Create a button to get the selected date and time
select_button = ttk.Button(root, text="Select Date Time", command=get_selected_datetime)
select_button.grid(row=1, columnspan=2, padx=10, pady=5)

root.mainloop()
