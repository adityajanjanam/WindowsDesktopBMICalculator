import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height * height)
        bmi_result.set(f"BMI: {bmi:.2f}")
        categorize_bmi(bmi)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    category_result.set(f"Category: {category}")

# Create the main application window
root = ttk.Window(themename="flatly")
root.title("BMI Calculator")
root.geometry("400x300")

# Create StringVars to hold the results
bmi_result = ttk.StringVar()
category_result = ttk.StringVar()

# Add styling and layout components
frame = ttk.Frame(root, padding=20)
frame.pack(fill=BOTH, expand=YES)

ttk.Label(frame, text="Weight (kg):", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
weight_entry = ttk.Entry(frame, font=("Helvetica", 12))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame, text="Height (cm):", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky=W)
height_entry = ttk.Entry(frame, font=("Helvetica", 12))
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi, bootstyle=PRIMARY)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

ttk.Label(frame, textvariable=bmi_result, font=("Helvetica", 14), bootstyle=SUCCESS).grid(row=3, column=0, columnspan=2, pady=5)
ttk.Label(frame, textvariable=category_result, font=("Helvetica", 14), bootstyle=INFO).grid(row=4, column=0, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()
