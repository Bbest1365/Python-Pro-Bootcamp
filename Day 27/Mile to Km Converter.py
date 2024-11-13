from tkinter import *

#Window

window = Tk()
window.title('Mile to Km converter')
window.minsize(200,200)
# window.config(padx=100, pady=50)

#Label
my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)
miles = Label(text="Miles")
miles.grid(column=2, row=0)
kilo = Label(text="Km")
kilo.grid(column=2, row=1)

#Entry

input1 = Entry(width=10)
input1.insert(END, string="0")
input1.grid(column=1,row=0)
# input2.grid(column=1,row=1)

# print(input1.get())
# print(input2.get())

#Button
def converter():
    new_text = float(input1.get())*1.609344
    km.config(text=new_text)

# result=input1.get()*1.609344
button = Button(text="Calculate",command=converter)
button.grid(column=1,row=2)


km = Label(text='0')
km.grid(column=1,row=1)








window.mainloop()