import tkinter as tk
from datetime import datetime, timedelta
from quakeFuncs import *
import ttkbootstrap as ttk
import random
import string
from operator import attrgetter
import ssl
from urllib.request import urlopen
from json import loads

def display_quakes(earthquakes):
    for widget in quakes_frame.winfo_children():
        widget.destroy()
    
    for quake in earthquakes:
        quake_label = ttk.Label(quakes_frame, text="(%.2f) %40s at %s (%.3f, %.3f)" % 
                                 (quake.mag, quake.place, time_to_str(quake.time), quake.longitude, quake.latitude), 
                                 font=("Times New Roman", 12))
        quake_label.pack(pady=5)
    
    quakes_canvas.update_idletasks()
    quakes_canvas.config(scrollregion=quakes_canvas.bbox("all"))

def sort_by_mag(quakes):
    quakes.sort(reverse=True)
    return quakes

def sort_by_time(quakes):
    quakes.sort(key=attrgetter('time'), reverse=True)
    return quakes

def sort_by_longitude(quakes):
    quakes.sort(key=attrgetter('longitude'))
    return quakes

def sort_by_latitude(quakes):
    quakes.sort(key=attrgetter('latitude'))
    return quakes

def filter_by_mag(quakes, low, high):
    return [quake for quake in quakes if (quake.mag <= high and quake.mag >= low)]

def filter_by_place(quakes, word):
    text = word.lower()
    return [quake for quake in quakes if (quake.place.lower().find(text) != -1)]

def sort_quakes():
    def apply_sort(option):
        global earthquakes
        if option == "Magnitude":
            earthquakes = sort_by_mag(earthquakes)
        elif option == "Time":
            earthquakes = sort_by_time(earthquakes)
        elif option == "Longitude":
            earthquakes = sort_by_longitude(earthquakes)
        elif option == "Latitude":
            earthquakes = sort_by_latitude(earthquakes)
        display_quakes(earthquakes)
    
    sort_window = tk.Toplevel(window)
    sort_window.title("Sort Options")
    sort_window.geometry("300x200")
    
    ttk.Label(sort_window, text="Sort by:", font='Calibri 16 bold').pack(pady=10)
    
    options = ["Magnitude", "Time", "Longitude", "Latitude"]
    selected_option = tk.StringVar(value=options[0])
    
    dropdown = ttk.Combobox(sort_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)
    
    apply_button = ttk.Button(sort_window, text="Apply", command=lambda: [apply_sort(selected_option.get()), sort_window.destroy()])
    apply_button.pack(pady=10)

def filter_quakes():
    def update_fields(*args):
        if selected_option.get() == "Magnitude":
            mag_frame.pack()
            search_frame.pack_forget()
        else:
            mag_frame.pack_forget()
            search_frame.pack()

    def apply_filter():
        global earthquakes
        if selected_option.get() == "Magnitude":
            low = float(low_entry.get())
            high = float(high_entry.get())
            earthquakes = filter_by_mag(earthquakes, low, high)
        elif selected_option.get() == "Place":
            word = search_entry.get()
            earthquakes = filter_by_place(earthquakes, word)
        display_quakes(earthquakes)
        filter_window.destroy()
    
    filter_window = tk.Toplevel(window)
    filter_window.title("Filter Options")
    filter_window.geometry("350x250")
    
    ttk.Label(filter_window, text="Filter by:", font='Calibri 16 bold').pack(pady=10)
    
    options = ["Magnitude", "Place"]
    selected_option = tk.StringVar(value=options[0])
    selected_option.trace_add("write", update_fields)
    
    dropdown = ttk.Combobox(filter_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)
    
    mag_frame = ttk.Frame(filter_window)
    ttk.Label(mag_frame, text="Low Magnitude:").grid(row=0, column=0, padx=5, pady=5)
    low_entry = ttk.Entry(mag_frame)
    low_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(mag_frame, text="High Magnitude:").grid(row=1, column=0, padx=5, pady=5)
    high_entry = ttk.Entry(mag_frame)
    high_entry.grid(row=1, column=1, padx=5, pady=5)
    
    search_frame = ttk.Frame(filter_window)
    ttk.Label(search_frame, text="Search Place:").grid(row=0, column=0, padx=5, pady=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5, pady=5)
    
    mag_frame.pack()
    
    apply_button = ttk.Button(filter_window, text="Apply", command=apply_filter)
    apply_button.pack(pady=10)

def get_json(url):
   gcontext = ssl.SSLContext() 
   with urlopen(url, context=gcontext) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def quake_from_feature(f):
	return Earthquake(f['properties']['place'], float(f['properties']['mag']), float(f['geometry']['coordinates'][0]), float(f['geometry']['coordinates'][1]), int((f['properties']['time']) / 1000))

def new_quakes():
	global earthquakes
	features = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')["features"]
	for feature in features:
		new_quake = quake_from_feature(feature)
		count = 0
		if (new_quake not in earthquakes):
			earthquakes.append(quake_from_feature(feature))
			count += 1

	display_quakes(earthquakes)

def save_data(quakes=None, filename='quakes.txt'):
    if quakes is None:
        quakes = earthquakes
    with open(filename, 'w') as outFile:
        for quake in quakes:
            outFile.write(str(quake.mag) + " " + str(quake.longitude) + " " + str(quake.latitude) + " " + str(quake.time) + " " + str(quake.place) + "\n")


def quit_quakes():
    global earthquakes
    save_data(earthquakes)
    window.destroy()

# window
window = ttk.Window(themename = 'darkly')
window.title("Live-Earthquake Dashboard")
window.geometry('1200x600')

# title
title_label = ttk.Label(master = window, text = 'Earthquakes', font= ('Segoe UI', 24, 'bold'), anchor="center", style='info.TLabel')
title_label.pack(pady=20)

# input field
input_frame = ttk.Frame(master = window)
sort_button = ttk.Button(master = input_frame, text = 'Sort', command = sort_quakes, style='info.TButton')
filter_button = ttk.Button(master = input_frame, text = 'Filter', command = filter_quakes, style='info.TButton')
new_button = ttk.Button(master = input_frame, text = 'New', command = new_quakes, style='info.TButton')
quit_button = ttk.Button(master = input_frame, text = 'Quit', command = quit_quakes, style='danger.TButton')
sort_button.pack(side = 'left', padx = 20)
filter_button.pack(side = 'left', padx = 20)
new_button.pack(side = 'left', padx = 20)
quit_button.pack(side = 'left', padx = 20)
input_frame.pack(pady = 10)

# Add a Scrollbar
quakes_frame_container = ttk.Frame(window)
quakes_frame_container.pack(fill='both', expand=True, padx=20, pady=10)

quakes_canvas = tk.Canvas(quakes_frame_container)
quakes_scrollbar = ttk.Scrollbar(quakes_frame_container, orient='vertical', command=quakes_canvas.yview)

quakes_frame = ttk.Frame(quakes_canvas)
quakes_frame.bind("<Configure>", lambda e: quakes_canvas.config(scrollregion=quakes_canvas.bbox("all")))

quakes_window = quakes_canvas.create_window((0, 0), window=quakes_frame, anchor='nw')
quakes_canvas.configure(yscrollcommand=quakes_scrollbar.set)

quakes_canvas.pack(side='left', fill='both', expand=True)
quakes_scrollbar.pack(side='right', fill='y')

earthquakes = read_quakes_from_file("quakes.txt")
display_quakes(earthquakes)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = "Password", 
	font = ('Segoe UI', 16), 
	textvariable = output_string,
	style='secondary.TLabel')
output_label.pack(pady = 10)

window.mainloop()