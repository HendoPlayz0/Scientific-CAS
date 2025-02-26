import tkinter as tk
from tkinter import ttk
import math

class HomeMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("VSC's Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#2C3E50')  # Dark blue background
        
        # Title Label
        title = tk.Label(root, text="VSC's Calculator", 
                        font=('Arial', 32, 'bold'), 
                        fg='#ECF0F1',  # White text
                        bg='#2C3E50')  # Dark blue background
        title.pack(pady=100)
        
        # Start Button
        start_button = tk.Button(root, text="Start Calculator", 
                               command=self.start_calculator,
                               font=('Arial', 16),
                               bg='#3498DB',  # Light blue
                               fg='white',
                               activebackground='#2980B9',  # Darker blue when clicked
                               padx=20, pady=10)
        start_button.pack(pady=50)

    def start_calculator(self):
        self.root.destroy()  # Close the home menu
        new_root = tk.Tk()
        calculator = ScientificCalculator(new_root)
        new_root.mainloop()

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#34495E')  # Dark blue-grey background
        
        # Create display with new styling
        self.display = tk.Entry(root, 
                              font=('Arial', 20), 
                              justify='right', 
                              bd=5,
                              bg='#ECF0F1',  # Light grey background
                              fg='#2C3E50')  # Dark text
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        
        # Button layout (rest of the code remains the same)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('√', 6, 0), ('log', 6, 1), ('ln', 6, 2), ('()', 6, 3),
            ('π', 7, 0), ('e', 7, 1), ('C', 7, 2), ('⌫', 7, 3)
        ]
        
        # Create styled buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
            
        # Configure grid
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            
    def create_button(self, text, row, col):
        # Custom styling for different button types
        if text in ['=']:
            bg_color = '#27AE60'  # Green
        elif text in ['C', '⌫']:
            bg_color = '#E74C3C'  # Red
        elif text in ['+', '-', '*', '/', '^']:
            bg_color = '#E67E22'  # Orange
        elif text in ['sin', 'cos', 'tan', 'log', 'ln', '√']:
            bg_color = '#9B59B6'  # Purple
        else:
            bg_color = '#3498DB'  # Blue
            
        button = tk.Button(self.root, 
                          text=text,
                          command=lambda: self.button_click(text),
                          font=('Arial', 12, 'bold'),
                          bg=bg_color,
                          fg='white',
                          activebackground='#2980B9',
                          width=6,
                          height=2)
        button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

    def button_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'C':
            self.display.delete(0, tk.END)
        elif text == '⌫':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        elif text in ['sin', 'cos', 'tan']:
            try:
                num = float(self.display.get())
                if text == 'sin':
                    result = math.sin(math.radians(num))
                elif text == 'cos':
                    result = math.cos(math.radians(num))
                else:
                    result = math.tan(math.radians(num))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == '√':
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'π':
            self.display.insert(tk.END, str(math.pi))
        elif text == 'e':
            self.display.insert(tk.END, str(math.e))
        elif text == 'log':
            try:
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'ln':
            try:
                result = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    home = HomeMenu(root)
    root.mainloop()