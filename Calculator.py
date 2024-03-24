import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields for numbers
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Dropdown for selecting operation
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation is addition
operation_dropdown = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_dropdown.grid(row=0, column=2, padx=5, pady=5)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
