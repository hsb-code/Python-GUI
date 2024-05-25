# Window
from tkinter import * # accessed tkinter module and classes
# we can use them to build GUI

window = Tk() # default window created with defualt size 200 x 200
window.geometry('350x500') # changing dimensions
window.title('Calculator') # changing title
window.configure(bg='#3fc4ae') # change color ; copied HEX value from color picker on google
window.iconbitmap('calculator_icon.ico') # change icon ; icon file and code file location must be the same

# Buttons
# the tkinter module let us create button and place them anywhere in window
# it also let you excute function when certain button is pressed

buttont = Button(window, width = 5, height = 5, text = '00000', relief = 'ridge', bg = '#5fe8d1', font = ('times new roman', 12))
buttont.pack(fill=X) # fillx means access the minimal space in x direction
# insert button using 1.pack, 2.place and 3.grid

equation = StringVar
entry0 = Entry(window, textvariable = equation, justify = 'right')
entry0.pack(ipadx=20) # space 20 units in x direction
# StringVar is a class in tkinter, it is used to monitor changes in string variable

# we cannot use two geometry managers in same window or frame
# we have to create another frame in window to use grid function
# Grid function
# arrange the buttons in rows and columns just like grid
button_frame = Frame(window)
button_frame.pack() # packing or inserting our frame to parent window

button0 = Button(button_frame, text = '0', relief = 'ridge')
button1 = Button(button_frame, text = '1', relief = 'ridge')
button2 = Button(button_frame, text = '2', relief = 'ridge')
button3 = Button(button_frame, text = '3', relief = 'ridge')

button0.grid(row = 0, column = 0)
button1.grid(row = 0, column = 1)
button2.grid(row = 1, column = 0)
button3.grid(row = 1, column = 1)

# Mapping
# columnspan is a function that allows a button to take space of two or more buttons
# when one widget takes space of two cells, it does not fill up the complete space
# it just takes two cells but does not properly filled it up
# so a function sticky with direction north, south, east and west is used to allocate a complete space

# Place function
# Place function allows you to place a button in window
# it splits the windows in x and y coordinates
# default coordinates are 00, at top left corner of screen

window.mainloop() # this tells python to run tkinter loop
# prevets any further code working untill the window is closed