from tkinter import*

def doNothing():
    print("ok, ok , i won't!")

def start():
    print("Ok, let's start your project:")

def refresh():
    print ("make refresh your computer")

def exit():
    quit()

    

def redo():
    print("plz redo some poject")
def image():
    print ("do u insert an image")
def Print():
    print("will u copy the image or print it")

root = Tk()
#*****Menu create*****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu=subMenu)
subMenu.add_command(label= "New project..$", command = doNothing)
subMenu.add_command(label="now..", command = start)
subMenu.add_command(label= "Refresh", command=refresh)
subMenu.add_separator()
subMenu.add_command(label="exit", command = quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=redo)

#*****Toolbar create****
toolbar = Frame(root, bg="red")
insertButt = Button(toolbar, text="insert Image", command =image)
insertButt.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Print", command=Print)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#***Adding the status bar***
status = Label(root, text="preparing to do nothing.....", bd=1, relief = SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()
