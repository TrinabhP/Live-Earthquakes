import tkinter as tk
import ttkbootstrap as ttk
import random
import string


def sort_quakes():
	pass

def filter_quakes():
	pass

# window
window = ttk.Window(themename = 'darkly')
window.title("Live-Earthquake Dashboard")
window.geometry('600x300')

# title
title_label = ttk.Label(master = window, text = 'Earthquakes', font= 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
sort_button = ttk.Button(master = input_frame, text = 'Sort', command = sort_quakes)
filter_button = ttk.Button(master = input_frame, text = 'Filter', command = filter_quakes)
new_button = ttk.Button(master = input_frame, text = 'New', command = sort_quakes)
quit_button = ttk.Button(master = input_frame, text = 'Quit', command = filter_quakes)
sort_button.pack(side = 'left', padx = 10)
filter_button.pack(side = 'left')
new_button.pack(side = 'left', padx = 10)
quit_button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = "Password", 
	font = 'Calibri 24', 
	textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()