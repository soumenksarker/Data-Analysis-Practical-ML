from tkinter import*
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Warning level", "Last warning, be passionate right now")
answer = tkinter.messagebox.askquestion("Alert!!", "Do u like to be silly?")
if answer == "yes":
    print("Fuck on your own ass")
root.mainloop()

