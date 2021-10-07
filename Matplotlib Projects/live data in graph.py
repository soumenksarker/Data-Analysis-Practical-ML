import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
import urllib
import json
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")
f =  Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

def animate(i):
    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode("utf-8")
    data = json.loads(data)
    data = data["btc_usd"]
    data = pd.DataFrame(data)
    buys = data[(data["type"]=="bid")]
    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
    buyDates = (buys["datestamp"]).tolist()
    
    sells =data[(data["type"]=="ask")]
    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
    sellDates = (sells["datestamp"]).tolist()
    a.clear()
    a.plot_date(buyDates, buys["price"],"r", label="buys")
    a.plot_date(sellDates, sells["price"],"g", label="sells")
    a.legend()#(bbox_to_anchor)
    title = "BTC-e BTCUSD Prices\nLast Price:" + str(data['price'][1999])
    a.set_title(title)

    
class SeaofBTCapp(tk.Tk):
 
     def __init__(self,*args, **kwargs):
         
         tk.Tk.__init__(self, *args, **kwargs)
         
         container = tk.Frame(self)
         
         container.pack(side = "top", fill="both", expand = True)

         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight =1)

         self.frames = {}
         
         for F in (StartPage, BTCe_Page):
              frame =F(container, self)
              self.frames[F] = frame
              frame.grid(row=0, column=0, sticky="nsew")
            
         self.show_frame(StartPage)

     def show_frame(self, cont):
          
         frame = self.frames[cont]
         frame.tkraise()
         
class StartPage(tk.Frame):
     
         def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          label = tk.Label(self, text = """Alpha bitcoin trading Application.Use at your own risk, there is no warrenty here!!!""" , font=LARGE_FONT)
          label.pack(pady=10, padx=10)
          button1 = ttk.Button(self, text="Agree",command=lambda: controller.show_frame(BTCe_Page))
          button1.pack()
          button2 = ttk.Button(self, text="Disagree",command = quit)
          button2.pack()
         
class PageOne(tk.Frame):
     
        def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          label = tk.Label(self, text = "Page One!!!", font=LARGE_FONT )
          label.pack(pady=10, padx=10)
        
          button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
          button1.pack()

class BTCe_Page(tk.Frame):
        def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          label = tk.Label(self, text = "Ok, now time for U!! Implement your thinking ,, what u wana create,,, incredible! Amazing! Animate it,,Let's start with Graphics! your ideas..", font=LARGE_FONT )
          label.pack(pady=10, padx=10)
        
          button1 = ttk.Button(self, text="Back to HOME", command=lambda: controller.show_frame(StartPage))
          button1.pack()
          
        

          canvas = FigureCanvasTkAgg(f, self)
          canvas.show()
          canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

          toolbar = NavigationToolbar2TkAgg(canvas, self)
          toolbar.update()
          canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

          
app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
           
     


                    
         
         
