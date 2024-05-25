from tkinter import *

window = Tk()
window.geometry('350x500')
window.title('Calculator')
window.configure(bg='#3fc4ae')
window.iconbitmap('calculator_icon.ico')

expression_frame = Frame(window, bg = '#3fc4ae')
button_frame = Frame(window, bg = '#3fc4ae')
expression_frame.pack()
button_frame.pack()

font_button = ('times new roman', 14,)
font_entry = ('arial', 20, 'bold')
equation = StringVar()
equation.set('0') # default value set to 0
equation_field = Entry(expression_frame, textvariable = equation, font = font_entry, justify = 'right')
equation_field.pack(ipadx=10, ipady=10, pady=20)

# button press function
expression = ''
def press(n):
    global expression
    expression += str(n)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = '' # to return to empty string, otherwise the entry will hold previous value
    except:
        equation.set('Undefined')
        expression = ''

def clear():
    global expression
    expression = ''
    equation.set(0)

def back():
    global expression
    expression = expression.rstrip(expression[-1]) # rstrip is a function that removes one strinf from right
    equation.set(expression)

button1 = Button(button_frame, text = '1', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(1))
button2 = Button(button_frame, text = '2', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(2))
button3 = Button(button_frame, text = '3', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(3))
plus = Button(button_frame, text = '+', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press('+'))
button4 = Button(button_frame, text = '4', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(4))
button5 = Button(button_frame, text = '5', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(5))
button6 = Button(button_frame, text = '6', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(6))
minus = Button(button_frame, text = '-', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press('-'))
button7 = Button(button_frame, text = '7', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(7))
button8 = Button(button_frame, text = '8', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(8))
button9= Button(button_frame, text = '9', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(9))
multiply = Button(button_frame, text = '*', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press('*'))
button0 = Button(button_frame, text = '0', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press(0))
decimal = Button(button_frame, text = '.', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press('.'))
clear = Button(button_frame, text = 'C', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = clear)
divide = Button(button_frame, text = '/', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = lambda : press('/'))
equal = Button(button_frame, text = '=', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = equal)
backspace = Button(button_frame, text = '<<', font = font_button, relief= 'ridge', bg = '#5fe8d1', borderwidth=1, width=8, height=3, command = back)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
plus.grid(row=0, column=3)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
minus.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
multiply.grid(row=2, column=3)

button0.grid(row=3, column=0)
decimal.grid(row=3, column=1)
clear.grid(row=3, column=2)
divide.grid(row=3, column=3)

equal.grid(row=4, column=0, columnspan=3, sticky='nsew')
backspace.grid(row=4, column=3)



window.mainloop()