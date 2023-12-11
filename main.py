import tkinter as tk
from tkinter import ttk

def convert():
    mile = input.get()
    output = mile * 1.609
    output_label["text"] = output

window = tk.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

input = tk.IntVar()

entry = ttk.Entry(window, width = 10, textvariable = input)
entry.grid(column = 1, row = 0)

miles_label = ttk.Label(window, text = "Miles")
miles_label.grid(column = 2, row = 0)

equal = ttk.Label(window, text = "Is equal to")
equal.grid(column = 0, row = 1)

output_label = ttk.Label(window, text = "0")
output_label.grid(column = 1, row = 1)

km_label = ttk.Label(window, text = "Km")
km_label.grid(column = 2, row = 1)

button = ttk.Button(window, text = "Calculate", command = convert)
button.grid(column = 1, row = 2)

window.mainloop()