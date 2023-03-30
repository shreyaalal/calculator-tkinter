import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")
        
        # Input Field
        self.input_field = tk.Entry(master)
        self.input_field.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Buttons
        self.add_button = tk.Button(master, text="+", command=self.add)
        self.add_button.grid(row=1, column=0)

        self.sub_button = tk.Button(master, text="-", command=self.subtract)
        self.sub_button.grid(row=1, column=1)

        self.mul_button = tk.Button(master, text="*", command=self.multiply)
        self.mul_button.grid(row=1, column=2)

        self.div_button = tk.Button(master, text="/", command=self.divide)
        self.div_button.grid(row=1, column=3)

        self.mod_button = tk.Button(master, text="%", command=self.modulo)
        self.mod_button.grid(row=2, column=0)

        self.clear_button = tk.Button(master, text="C", command=self.clear)
        self.clear_button.grid(row=2, column=1)

        self.equals_button = tk.Button(master, text="=", command=self.calculate)
        self.equals_button.grid(row=2, column=2, columnspan=2)
        
        # Output Field
        self.output_field = tk.Entry(master)
        self.output_field.grid(row=3, column=0, columnspan=4, pady=10)
        
    def add(self):
        self.operation = "+"
        self.first_number = float(self.input_field.get())
        self.input_field.delete(0, tk.END)

    def subtract(self):
        self.operation = "-"
        self.first_number = float(self.input_field.get())
        self.input_field.delete(0, tk.END)

    def multiply(self):
        self.operation = "*"
        self.first_number = float(self.input_field.get())
        self.input_field.delete(0, tk.END)

    def divide(self):
        self.operation = "/"
        self.first_number = float(self.input_field.get())
        self.input_field.delete(0, tk.END)
        
    def modulo(self):
        self.operation = "%"
        self.first_number = float(self.input_field.get())
        self.input_field.delete(0)
