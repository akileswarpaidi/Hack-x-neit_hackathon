import webbrowser
import tkinter as tk
from tkinter import ttk

# Replace YOUR_API_KEY with your actual API key
API_KEY = "AIzaSyC0E2-VFWnUjcoN63GjKLE-QZI94kcjEaU"

def submit():
    origin = origin_entry.get()
    destination = destination_entry.get()
    mode = mode_combo.get()
    url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode={mode}&key={API_KEY}"
    webbrowser.open_new(url)

# Create a Tkinter window with the source and destination inputs, mode of transportation dropdown, and submit button
window = tk.Tk()
window.title("Google Maps")
window.geometry("300x200")
window.configure(bg="#F0F0F0")
# window.iconbitmap('icon.ico')  # Replace 'icon.ico' with the path to your icon file
window.config(bg='#0077CC')  # Set the background color of the window to blue

style = ttk.Style()
style.configure("TLabel", background="#F0F0F0", foreground="#0077CC", font=("Arial", 12))
style.configure("TButton", background="#0077CC", foreground="black", font=("Arial", 12))

origin_label = ttk.Label(window, text="Source:")
origin_label.pack(pady=5)

origin_entry = ttk.Entry(window, font=("Arial", 12))
origin_entry.pack(pady=5)

destination_label = ttk.Label(window, text="Destination:")
destination_label.pack(pady=5)

destination_entry = ttk.Entry(window, font=("Arial", 12))
destination_entry.pack(pady=5)

mode_label = ttk.Label(window, text="Mode of Transportation:")
mode_label.pack(pady=5)

mode_options = ["driving", "walking", "bicycling", "transit"]
mode_combo = ttk.Combobox(window, values=mode_options, font=("Arial", 12))
mode_combo.pack(pady=5)

submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=10)

window.mainloop()
