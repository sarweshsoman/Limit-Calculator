import tkinter as tk
from tkinter import ttk
import sympy as sp

class LimitCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Limit Calculator')

        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12), padding=(5, 5))
        style.configure('TEntry', font=('Arial', 12), padding=(5, 5))
        style.configure('TButton', font=('Arial', 12), padding=(5, 5))

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text='Symbol:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.symbol_text = ttk.Entry(self.root)
        self.symbol_text.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(self.root, text='Limit:').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.limit_text = ttk.Entry(self.root)
        self.limit_text.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(self.root, text='Expression:').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.expression_text = ttk.Entry(self.root)
        self.expression_text.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        ttk.Button(self.root, text='Calculate', command=self.calculate_limit).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.result_label = ttk.Label(self.root, text='Result:')
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate_limit(self):
        try:
            symbol_str = self.symbol_text.get()
            limit_str = self.limit_text.get()
            expression_str = self.expression_text.get()

            if not (symbol_str and limit_str and expression_str):
                raise ValueError("Please enter values for symbol, limit, and expression.")

            sym = sp.symbols(symbol_str)
            expression = f'{expression_str}.doit()' if "Sum" in expression_str else expression_str

            lim = sp.limit(expression, sym, limit_str)
            self.result_label.config(text=f'Result: {lim}')

        except (sp.SympifyError, ValueError) as e:
            self.result_label.config(text=f'Error: {str(e)}')

if __name__ == "__main__":
    LimitCalculator().root.mainloop()
