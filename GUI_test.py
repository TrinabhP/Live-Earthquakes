import tkinter as tk
from datetime import datetime, timedelta
from quakeFuncs import *
import ttkbootstrap as ttk
import random
import string


def display_quakes(earthquakes):
	rows = 1
	for quake in earthquakes:
		current_quakes = ttk.Label(window, text="(%.2f) %40s at %s (%.3f, %.3f)" % (quake.mag, quake.place, time_to_str(quake.time), quake.longitude, quake.latitude), font=("Times New Roman", 12))
		current_quakes.pack(pady = 10)
		rows += 1

def sort_quakes():
	pass

def filter_quakes():
	pass

def new_quakes():
	pass

def quit_quakes():
	window.destroy()

# window
window = ttk.Window(themename = 'darkly')
window.title("Live-Earthquake Dashboard")
window.geometry('1200x600')

# title
title_label = ttk.Label(master = window, text = 'Earthquakes', font= 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
sort_button = ttk.Button(master = input_frame, text = 'Sort', command = sort_quakes)
filter_button = ttk.Button(master = input_frame, text = 'Filter', command = filter_quakes)
new_button = ttk.Button(master = input_frame, text = 'New', command = new_quakes)
quit_button = ttk.Button(master = input_frame, text = 'Quit', command = quit_quakes)
sort_button.pack(side = 'left', padx = 10)
filter_button.pack(side = 'left')
new_button.pack(side = 'left', padx = 10)
quit_button.pack(side = 'left')
input_frame.pack(pady = 10)


earthquakes = read_quakes_from_file("quakes.txt")
display_quakes(earthquakes)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = "Password", 
	font = 'Calibri 24', 
	textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()