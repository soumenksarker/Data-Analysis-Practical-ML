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
from matplotlib import pyplot as plt

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
f =  Figure()
a = f.add_subplot(111)

exchange = "BTC-e"
DatCounter = 9000
programName = "btc"

resampleSize = "1Min"
DataPace = "1d"
candelWidth = "0.008"

def changeTimeFrame (tf):
    global DataPace
    global DatCounter
    if DataPace == "7d" and resamplesize == "1Min":
        popupmsg ("Too much data chosen, chose a smaller size of data frame or higher look up OHLCI interval" )
    else:
        DataPace = tf
        DatCounter = 9000


def changeSampleSize(size, width):
    global resampleSize
    global DatCounter
    global CandleWidth
    global DataPace
    if DataPace== "7d" and resamplesize == "1Min":
        popupmsg ("Too much data chosen, chose a smaller size of data frame or take higher OHLCI interval")

    elif DataPace == "tick":
        print ("U r viewing the tick data not OHLCI.")
    else:
        resampleSize = size
        DatCounter = 9000
        CandleWidth = width 
def changeExchange(toWhat, pn):
    global exchange
    global DataCounter
    global programName

    exchange = toWhat
    programname = pn
    DataCounter = 9000

def popupmsg(msg):
    popup = tk.Tk()
    #def leavemini():
       # pop.destroy()
        
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okey", command= popup.destroy)
    B1.pack()
    popup.mainloop()
    
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
         
         menubar = tk.Menu(container)
         filemenu = tk.Menu(menubar, tearoff=0)
         filemenu.add_command(label="Save settings", command = lambda:popupmsg("Not supported just yet!"))
         filemenu.add_separator()
         filemenu.add_command(label="Exit", command=quit)
         menubar.add_cascade(label="File", menu=filemenu)
         exchangeChoice = tk.Menu(menubar, tearoff=1)

         exchangeChoice.add_command(label = "BTC-e", command = lambda:changeExchange("BTC-e", "btce"))
         exchangeChoice.add_command(label = "Bitfinex", command = lambda:changeExchange("Bitfinex", "bitfinex"))
         exchangeChoice.add_command(label = "Bitstamp", command = lambda:changeExchange("Bitstamp", "bitstamp"))
         exchangeChoice.add_command(label = "Huobi", command = lambda:changeExchange("Huobi", "huobi"))
         menubar.add_cascade(label = "Change Exchange", menu=exchangeChoice)
                                    
         dataTF = tk.Menu(menubar, tearoff=1)
         dataTF.add_command(label = "Tick", command = lambda:changeTimeFrame("tick"))
         dataTF.add_command(label = "1 DAY", command = lambda:changeTimeFrame("1d"))
         dataTF.add_command(label = "3 DAY", command = lambda:changeTimeFrame("3d"))
         dataTF.add_command(label = "1 WEEK", command = lambda:changeTimeFrame("7d"))
         menubar.add_cascade(label = "Data Time Frame", menu = menubar)

         OHLCI = tk.Menu(menubar, tearoff=1)
         OHLCI.add_command(label = "Tick", command = lambda:changeTimeFrame("tick"))
         OHLCI.add_command(label = "1 min", command = lambda:changeTimeFrame("1Min", 0.0005))
         OHLCI.add_command(label = "5 min ", command = lambda:changeTimeFrame("5Min", 0.003))
         OHLCI.add_command(label = "15 min", command = lambda:changeTimeFrame("15Min", 0.008))
         OHLCI.add_command(label = "30 min", command = lambda:changeTimeFrame("30Min", 0.016))
         OHLCI.add_command(label = "1 hour", command = lambda:changeTimeFrame("1H", .032))
         OHLCI.add_command(label = "3 hour", command = lambda:changeTimeFrame("3H", 0.86))
         menubar.add_cascade(label = "OHLCI Time Interval", menu=OHLCI)
         


         
         tk.Tk.config(self, menu=menubar)
         
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
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()
           
     


                    
         
         
