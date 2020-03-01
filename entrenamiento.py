from tkinter import *
from tkcalendar import *


root = Tk()

text1 = Label(root,
                    text="PLANILLA DE ENTRENAMIENTO",
                    bg="grey",
                    fg="white",
                    font=("Times", 20))

text1.pack(fill="both")

text2 = Label(root,
                    text="EJERCICOS:",
                    bg="grey",
                    fg="white",
                    font=("Times", 20))

text2.pack(fill="both")


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

var = IntVar()
R1 = Radiobutton(root, text="EJERCICIO 1", variable=var, value=1,
                  command=sel)
R1.pack()

R2 = Radiobutton(root, text="EJERCICIO 2", variable=var, value=2,
                  command=sel)
R2.pack()

R3 = Radiobutton(root, text="EJERCICIO 3", variable=var, value=3,
                  command=sel)
R3.pack()

cal = Calendar(root, font="Arial 14", selectmode="day", year=2019, month=5, day=17)
cal.pack()

root.title("PSQ - GUI")
root.geometry("1680x1000+0+0")
root.mainloop()
