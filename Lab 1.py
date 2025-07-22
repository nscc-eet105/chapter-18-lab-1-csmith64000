#Chris Smith
# Chapter 18 - Lab 1
# 07/22/2025

import tkinter as tk

class FeetToInchesApp:
    def __init__(self, master):
        master.title("Feet and Inches Converter")

        # Labels
        self.title_label = tk.Label(master, text="Feet and Inches Converter")
        self.feet_label = tk.Label(master, text="Feet:")
        self.inches_label = tk.Label(master, text="Inches:")
        self.output_label = tk.Label(master, text="Inches:")

        # Entry boxes
        self.feet_entry = tk.Entry(master)
        self.inches_entry = tk.Entry(master)

        # Buttons
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)

        # Setup
        self.title_label.grid(row=0, column=0, columnspan=2, pady=5)
        self.feet_label.grid(row=1, column=0, sticky="e")
        self.feet_entry.grid(row=1, column=1)
        self.inches_label.grid(row=2, column=0, sticky="e")
        self.inches_entry.grid(row=2, column=1)
        self.output_label.grid(row=3, column=0, columnspan=2, pady=5)
        self.convert_button.grid(row=4, column=0, pady=5)
        self.exit_button.grid(row=4, column=1, pady=5)

    def convert(self):
        # Data
        feet = self.feet_entry.get()
        inches = self.inches_entry.get()

        # Conversion
        if feet.isdigit() and inches.isdigit():
            total = int(feet) * 12 + int(inches)
            self.output_label.config(text="Inches: " + str(total))
        else:
            self.output_label.config(text="Inches: Invalid input")

# Run the program
root = tk.Tk()
app = FeetToInchesApp(root)
root.mainloop()
    
