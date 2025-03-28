from tkinter import *
from datetime import datetime, timedelta


root = Tk()

root.title("Live-Earthquake Dashboard")
root.geometry('800x600')

time = Label(root, text=datetime.now().strftime("Time Now:\n%A, %B %d, %Y at %I:%M %p"))
time.pack()

sort_button = Button(root, text='Sort')
sort_button.pack()

filter_button = Button(root, text='Filter')
filter_button.pack()

newquakes_button = Button(root, text='New Earthquakes')
newquakes_button.pack()

def saveFile():
	message = Label(root, text="Saved to File")
	message.pack()


quit_button = Button(root, text='Quit', command=saveFile, fg='red')
quit_button.pack()


root.mainloop()

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
