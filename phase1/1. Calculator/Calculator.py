import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create an Entry widget for user input
entry = tk.Entry(app, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+" 
]

row_val, col_val = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(app, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(app, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, padx=20, pady=20, command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
