import tkinter as tk
import math

class AdvancedCalculator:
    # Initialize the calculator
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Expression and input text variable
        self.expression = ""
        self.input_text = tk.StringVar()

        # Display
        input_frame = tk.Frame(self.root, bd=2, relief="ridge")
        input_frame.pack(side="top", fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 24), bd=5, relief="sunken", justify="right")
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=15, fill="both")

        # Buttons
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        # Button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["sqrt", "sin", "cos", "tan"],
            ["log", "log10", "^", "C"]
        ]

        # Create buttons
        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                b = tk.Button(btns_frame, text=btn_text, width=8, height=3,
                              command=lambda txt=btn_text: self.on_button_click(txt))
                b.grid(row=r, column=c, padx=5, pady=5)

    # Button click handler
    def on_button_click(self, char):
        if char == "C": # Clear the input
            self.expression = ""
            self.input_text.set("")
        elif char == "=": # Evaluate the expression
            try:
                result = eval(self.expression.replace("^", "**")) # Handle exponentiation
                self.input_text.set(str(result))
                self.expression = str(result)
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        elif char in ["sqrt", "sin", "cos", "tan", "log", "log10"]:
            try: # Handle advanced functions
                if self.expression == "":
                    return
                value = float(self.expression)
                if char == "sqrt":
                    result = math.sqrt(value)
                elif char == "sin":
                    result = math.sin(value)
                elif char == "cos":
                    result = math.cos(value)
                elif char == "tan":
                    result = math.tan(value)
                elif char == "log":
                    result = math.log(value)
                elif char == "log10":
                    result = math.log10(value)

                self.input_text.set(str(result))
                self.expression = str(result)
            except Exception: # Handle errors like invalid input or math domain errors
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char) # Append the character to the expression
            self.input_text.set(self.expression)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = AdvancedCalculator(root)
    root.mainloop() # Start the GUI event loop
