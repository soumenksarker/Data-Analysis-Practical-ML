from tkinter import*

class SuptoButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text ="print the message:", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print ("wow, this is actualy  worked" )
        print("i wanna fly on the sky")

root = Tk()
b= SuptoButtons(root)
root.mainloop()

        
