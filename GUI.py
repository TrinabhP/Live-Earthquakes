from tkinter import *

from datetime import datetime, timedelta
from quakeFuncs import *


def display(earthquakes):
	root = Tk()

	root.title("Live-Earthquake Dashboard")
	root.geometry('1000x800')

	root.columnconfigure(0, weight=1)
	root.columnconfigure(1, weight=1)
	root.columnconfigure(2, weight=1)

	title = Label(root, text="Earthquakes:\n-------------------------", font=("Times New Roman bold", 20), padx=0, pady=5)
	title.grid(row=0, column=1, columnspan=1, pady=20, sticky='w')

	time = Label(root, text=datetime.now().strftime("Time Now:\n%A, %B %d, %Y at %I:%M %p"))
	time.grid(row=0,column=0, sticky='w')




	sort_button = Button(root, text='Sort', font="Arial")
	sort_button.grid(row=1, column=0, padx=10, pady=45, sticky='w')

	filter_button = Button(root, text='Filter', font="Arial")
	filter_button.grid(row=2, column=0, padx=10, pady=45, sticky='w')
	 
	newquakes_button = Button(root, text='New Earthquakes', font="Arial")
	newquakes_button.grid(row=3, column=0, padx=10, pady=45, sticky='w')


	def saveFile():
		message = Label(root, text="Saved to File")
		message.grid(row=5, column=0, sticky='w')


	quit_button = Button(root, text='Quit', command=saveFile, fg='red', font="Arial")
	quit_button.grid(row=4, column=0, padx=10, pady=45, sticky='w')

	rows = 1
	for quake in earthquakes:
	    current_quakes = Label(root, text="(%.2f) %40s at %s (%.3f, %.3f)" % (quake.mag, quake.place, time_to_str(quake.time), quake.longitude, quake.latitude), font=("Times New Roman", 12))
	    current_quakes.grid(row=rows, column=1, sticky='n')
	    rows += 1




	root.mainloop()


earthquakes = read_quakes_from_file("quakes.txt")
display(earthquakes)

"""
def display():
	# Creates the window
	root = Tk()
	root.geometry("1000x800")
	# Creates entry box
	e = Entry(root, width=50, borderwidth=5, fg="green")
	# Adds Text Inside entry box
	e.insert(0, "Enter Your Name: ")

	def myClick():
		hello = "Hello " + e.get()
		myLabel = Label(root, text=hello)
		myLabel.grid(row=4, column=10)

	# Creates a button
	myButton = Button(root, text="Enter Your Name", command=myClick, fg="blue")

	# Creating a Label Widget
	title = Label(root, text="Saved Earthquakes\n")
	past_quakes = Label(root, text="Previous Earthquakes")




	# positions text
	e.grid(row=0, column=100)
	title.grid(row=1, column=5)
	past_quakes.grid(row=2, column=5)
	myButton.grid(row=3, column=5)



	# Loops the program
	root.mainloop()

display()
"""
