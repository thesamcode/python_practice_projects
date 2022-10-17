
from tkinter import Tk, Button, Label, DoubleVar, Entry

# created the window variable. Created applicaiton container.
window = Tk()
# adds a title to the application window
window.title("Feet to Meter Conversion App")
# setting the background color for the app window
window.configure(background="light green")
#  setting the size for the window.
window.geometry("320x220")
#  this prevents the window from being resizable by the user
window.resizable(width=False, height=False)


def convert():
    # this is set tot he value that will be input for the feet value. Gets the value intered into widget and convert it to floating point number.
    value = float(ft_entry.get())
    meter = value * 0.3048
    # need to set the value into the entry widget for the meter box. Set the result to 4 decimals spaces as well.
    mt_value.set("%.4f" % meter)

# creating a function that clears the boxes
def clear():
    ft_value.set("")
    mt_value.set("")


# created a lbl variable. It is a LAbel widget. Need to specify the window, specify text on label, label background color, foreground color set, give label a width.
ft_lbl = Label(window,text="Feet",bg="purple",fg="white",width=14)
#  need to position the label inside the application container, use the grid function. Positioning it on column 0 row 0, adding some space horizontally, and adding some space vertically.
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

# position an entry widget on the same line as the label for it.
# the data type is a whole numbe or floating number
ft_value = DoubleVar()
# Want to create the entry widget in the window. Define data type for the entry. 
ft_entry = Entry(window,textvariable=ft_value,width=14)
# positioning the entry widget to be on the same row as the label for it.
ft_entry.grid(column=1, row=0)
# using this to clear the entry widget so it is clear when the application launches
ft_entry.delete(0,'end')

# Do this again for a new variable to create another set of label and entry widget.
mt_lbl = Label(window,text="Meter",bg="brown",fg="white",width=14)
mt_lbl.grid(column=0,row=1)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=30)
mt_entry.delete(0,'end')

# create a button. Window where button is to be created. Command is the function call for the button.
convert_btn = Button(window,text="Convert",bg="blue",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)

clear_btn = Button(window,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=30)

















# this runs the application
window.mainloop()