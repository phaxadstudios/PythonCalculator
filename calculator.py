import tkinter as tk
from tkinter import messagebox

class ComplexCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display frame
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        # Input field inside the display frame
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of the input field

        # Button frame
        button_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        button_frame.pack()

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=1, pady=1)

    def button_click(self, item):
        if item == "=":
            self.calculate()
        elif item == "C":
            self.clear()
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))  # Use eval() for simple mathematical calculations
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ComplexCalculator(root)
    root.mainloop()
