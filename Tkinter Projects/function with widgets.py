from tkinter import*

root = Tk()

def printName(event):
 print ("MY NAME IS SOUMEN")
button_1 = Button(root, text="print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()

