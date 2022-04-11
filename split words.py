import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")
s=USER_INP
new_str= s.split(',')
print(new_str)