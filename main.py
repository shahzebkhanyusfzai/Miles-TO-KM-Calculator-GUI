from tkinter import *

def Calculate_KM():
    value = float(input.get())
    km = value*1.609
    kmvalue.config(text=km)


window = Tk()
window.config(padx=30,pady=30)
window.title('Miles To KM Converter')
window.minsize(width = 250,height = 150)
kmvalue = Label(text="0")
kmvalue.grid(column=1,row=1)

Miles = Label(text="Miles")
Miles.grid(row=0,column=2)
Km = Label(text="KM")
Km.grid(row=1,column=2)
is_equal_to = Label(text="is_equal_to")
is_equal_to.grid(row=1,column=0)

input = Entry(window,width=10)
input.grid(row=0,column=1)
input.focus()
Calculate_btn = Button(window,text="Calculate",command=Calculate_KM)
Calculate_btn.grid(row=3,column=1)

window.mainloop()
