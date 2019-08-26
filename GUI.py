#-----------------------------------------Tkinter----------------------------------------------------------------------
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

#-------------------------------------------json-----------------------------------------------------------------------
import json    
#-----------------------------------------------Matplotlib-------------------------------------------------------------
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
#-------------------------------------------Data Processing--------------------------------------------------------------
import pandas as pd
import numpy as np
#-------------------------------------------Fire Base Part-------------------------------------------------------------
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
cred = credentials.Certificate("./teenscancode-caee5-firebase-adminsdk-ip0g2-e7d0d8e474.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://teenscancode-caee5.firebaseio.com'
})

Sensor_1_ref = db.reference('Sensor_1')
Sensor_2_ref = db.reference('Sensor_2')
ONOFF_ref = db.reference('ONOFF')
Difference_ref = db.reference('Difference')
Temperature_ref = db.reference('Temperature')
Altitude_ref = db.reference('Altitude')
Humidity_ref = db.reference('Humidity')
AQ_ref = db.reference('AQ')
AQ_stat_ref = db.reference('AQ_stat')
UV_ref = db.reference('UV')
#--------------------------------------------Other-----------------------------------------------------------------
import time
import datetime
import requests
#-----------------------------------------MatplotlibFigureSetup--------------------------------------------------------------
f_1 = Figure(figsize=(6,4), dpi=80)
f_2 = Figure(figsize=(6,4), dpi=80)
f_3 = Figure(figsize=(6,4), dpi=80)
f_Temp = Figure(figsize=(6,4), dpi=80)
f_HU = Figure(figsize=(6,4), dpi=80)
f_AQ = Figure(figsize=(6,4), dpi=80)
f_UV = Figure(figsize=(6,4), dpi=80)
a = f_1.add_subplot(111)
b = f_2.add_subplot(111)
c = f_3.add_subplot(111)
d = f_Temp.add_subplot(111)
f = f_HU.add_subplot(111)
g = f_AQ.add_subplot(111)
h = f_UV.add_subplot(111)




style.use("ggplot")

#-----------------------------AnimationOfGraph-----------------------------------------------------------------------

        
def animate(i):
    
    global Diffenent
    data = json.load(open('DATA.json','r'))
    data = pd.DataFrame(data)
    
    data["datestamp"] = np.array(data["timestamp"]).astype("datetime64[s]")
    dataDate = (data["datestamp"]).tolist()
    Diffenent = data["sensor_1"] - data["sensor_2"]
    a.clear()
    b.clear()
    c.clear()
    d.clear()        
    f.clear()
    g.clear()
    h.clear()
    
#-----------------------------------GraphTitle----------------------------------------------------------------------    
    a.plot_date(dataDate, data["sensor_1"], "g" , label = "Sensor 1")
    b.plot_date(dataDate, data["sensor_2"], "r" , label = "Sensor 2")
    c.plot_date(dataDate, Diffenent, "b" , label = "Diffenent")
    d.plot_date(dataDate, data["Temperature"], "b" , label = "Temperature")        
    f.plot_date(dataDate, data["Humidity"], "b" , label = "Altitude_refHumidity")
    g.plot_date(dataDate, data["AQ"], "b" , label = "AQ")
    h.plot_date(dataDate, data["UV"], "b" , label = "UV")
   
    title_1 = "Sensor One Graph" 
    title_2 = "Sensor Two Graph"
    title_3 = "Difference Of Water Current"
    title_4 = "Temperature"       
    title_6 = "Humidity"
    title_7 = "Air Quality"
    title_8 = "UV Index"
        
    a.set_title(title_1 + '\n' + ' L/Hour')
    b.set_title(title_2 + '\n' + ' L/Hour')
    c.set_title(title_3 + '\n' + ' L/Hour')
    d.set_title(title_4 + '\n' + ' °C')       
    f.set_title(title_6 + '\n' + ' %')
    g.set_title(title_7)
    h.set_title(title_8)
            
#------------------------------AQ&UV-Setup--------------------------------------------------------------       
def animate1(i):
    global Air_St
    global UV_St
    
    if(AQ_stat_ref.get() == 0):
        Air_St = 'Fresh Air'
        AQ_labela.config(fg = '#00FF00')
    elif(AQ_stat_ref.get() == 1):
        Air_St = 'Low Pollution'
        AQ_labela.config(fg = '#ff7f16')
    elif(AQ_stat_ref.get() == 2):
        Air_St = 'High Pollution'
        AQ_labela.config(fg = '#8B008B')
    elif(AQ_stat_ref.get() == 3):
        Air_St = 'Extremely Pollution'
        AQ_labela.config(fg = '#3f0000')
        
    if(UV_ref.get() == 0 or 1 or 2):
        UV_St = 'Low'
        UV_labela.config(fg = '#00FF00')
    elif(UV_ref.get() == 3 or 4 or 5):
        UV_St = 'Moderate'
        UV_labela.config(fg = '#f6ff00')
    elif(UV_ref.get() == 6 or 7):
        UV_St = 'High'
        UV_labela.config(fg = '#ffa500')
    elif(UV_ref.get() == 8 or 9 or 10):
        UV_St = 'Very High'
        UV_labela.config(fg = '#ff2100')
    elif(UV_ref.get() == 11 or 12):
        UV_St = 'Extreme'
        UV_labela.config(fg = '#a14bf2')
    
#-----------------------------TextOfChangingVar------------------------------------------------------
        
       
    Time_label.config(text= 'Current Local Time:\n' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n')
    Time_label_1.config(text= 'Current Local Time:\n' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n')
    Temperature_labela.config(text =  str(Temperature_ref.get()) +'°C')
    Humidity_labela.config(text =   str(Humidity_ref.get()) +'%')
    AQ_labela.config(text =  str(AQ_ref.get()) + '\n' +Air_St)
    UV_labela.config(text =  str(UV_ref.get()) + '\n' +UV_St)
    Altitude_label.config(text = 'Device Altitude:' + str(Altitude_ref.get())+'m' +'\n')
    Altitude_label_1.config(text = 'Device Altitude:' + str(Altitude_ref.get())+'m' +'\n')
    sensor1_labela.config(text = str(Sensor_1_ref.get())+'L/Hour')
    sensor2_labela.config(text = str(Sensor_2_ref.get())+'L/Hour')
    difference_labela.config(text = str(Difference_ref.get())+'L/Hour')
    if(ONOFF_ref.get() == 'Y'):
        PStatus_label.config(text = 'ON',bg = 'green')
    elif(ONOFF_ref.get() == 'N'):
        PStatus_label.config(text = 'OFF',bg = 'RED')
        
        
            
#---------------------------------------------GUI-Class--------------------------------------
    
      

class PipeChecking(tk.Tk):
    def __init__(self, *a, **k):
        tk.Tk.__init__(self, *a, **k)
        container = tk.Frame(self)
        container.pack(fill="both", expand = True)
        container.grid_rowconfigure(10,weight=1)
        container.grid_columnconfigure(10,weight=1)
        self.frames = {}
        for F in (Page1,Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 10, column = 10, sticky="nsew")
        self.show_frame(Page1)
        
    def show_frame(self, cout):
        frame = self.frames[cout]
        frame.tkraise()
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
 
#-----------------------------------------------------Page1------------------------------------------------------------
 
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        global Time_label_1
        global Altitude_label
        global Temperature_labela
        global Humidity_labela
        global AQ_labela
        global UV_labela
        
        
        tk.Frame.__init__(self, parent)
        
        
        title_1 = tk.Label(self, text= 'Street Condition\n', font= ("Verdana",10))
        title_1.grid(row = 0,column = 0,columnspan = 3)
        Time_label_1 = tk.Label(self, font= ("Verdana",8))
        Time_label_1.grid(row = 1,column = 0,columnspan = 3)
        
        Altitude_label = tk.Label(self, font= ("Verdana",8))
        Altitude_label.grid(row = 2,column = 0,columnspan = 3,sticky ='e')        
        Temperature_label = tk.Label(self,text = 'Current Temperature' ,font= ("Verdana",8))
        Temperature_label.grid(row = 3,column = 0)
        Temperature_labela = tk.Label(self, font= ("Verdana",8))
        Temperature_labela.grid(row = 4,column = 0)
        Humidity_label = tk.Label(self,text = 'Current Relative Humidity', font= ("Verdana",8))
        Humidity_label.grid(row = 3,column = 1)
        Humidity_labela = tk.Label(self, font= ("Verdana",8))
        Humidity_labela.grid(row = 4,column = 1)
        AQ_label = tk.Label(self,text = 'Current Air Quality' ,  font= ("Verdana",8))
        AQ_label.grid(row = 3,column = 2)
        AQ_labela = tk.Label(self, font= ("Verdana",8))
        AQ_labela.grid(row = 4,column = 2)
        UV_label = tk.Label(self,text = 'Current UV Index' ,  font= ("Verdana",8))
        UV_label.grid(row = 6,column = 0)
        UV_labela = tk.Label(self, font= ("Verdana",8))
        UV_labela.grid(row = 7,column = 0)
        
        Temp_canvas = FigureCanvasTkAgg(f_Temp, self)
        Temp_canvas.draw()
        Temp_canvas.get_tk_widget().grid(row = 5,column = 0)
        Humidity_canvas = FigureCanvasTkAgg(f_HU, self)
        Humidity_canvas.draw()
        Humidity_canvas.get_tk_widget().grid(row = 5,column = 1)
        AQ_canvas = FigureCanvasTkAgg(f_AQ, self)
        AQ_canvas.draw()
        AQ_canvas.get_tk_widget().grid(row = 5,column = 2)
        UV_canvas = FigureCanvasTkAgg(f_UV, self)
        UV_canvas.draw()
        UV_canvas.get_tk_widget().grid(row = 8,column = 0)
        
        button1 = tk.Button(self, text="Go To Pipe Leaking Checking System",
                            command=lambda: controller.show_frame(Page2), font= ("Verdana",10))
        button1.grid(row = 8,columnspan = 3)

#------------------------------------------------Page2-----------------------------------------------------------
        
class Page2(tk.Frame):

    def __init__(self, parent, controller):
        global Time_label
        global sensor1_labela
        global sensor2_labela
        global difference_labela
        global Altitude_label_1
        global PStatus_label
        
        tk.Frame.__init__(self, parent)
        
        title_1 = tk.Label(self, text= 'Pipe Checking System\n', font= ("Verdana",10))
        title_1.grid(row = 0,column = 0,columnspan = 3)
        Time_label = tk.Label(self, font= ("Verdana",8))
        Time_label.grid(row = 1,column = 0,columnspan = 3)
        
        Altitude_label_1 = tk.Label(self, font= ("Verdana",8))
        Altitude_label_1.grid(row = 2,column = 0,columnspan = 3,sticky ='e')        
        sensor1_label = tk.Label(self,text = 'Sensor One Current' ,font= ("Verdana",8))
        sensor1_label.grid(row = 3,column = 0)
        sensor1_labela = tk.Label(self, font= ("Verdana",8))
        sensor1_labela.grid(row = 4,column = 0)
        sensor2_label = tk.Label(self,text = 'Sensor Two Current', font= ("Verdana",8))
        sensor2_label.grid(row = 3,column = 1)
        sensor2_labela = tk.Label(self, font= ("Verdana",8))
        sensor2_labela.grid(row = 4,column = 1)
        difference_label = tk.Label(self,text = 'Current Difference' ,  font= ("Verdana",8))
        difference_label.grid(row = 3,column = 2)
        difference_labela = tk.Label(self, font= ("Verdana",8))
        difference_labela.grid(row = 4,column = 2)
        Control_label = tk.Label(self,text = 'To ON or OFF the PUMP----->', font= ("Verdana",8))
        Control_label.grid(row = 6,column = 0,columnspan=2,rowspan = 2,sticky = 'e')
        Status_label = tk.Label(self,text = 'Status Of The Pump:', font= ("Verdana",10))
        Status_label.grid(row = 8,column = 0,columnspan=2,rowspan = 2,sticky = 'e')
        PStatus_label = tk.Label(self, font= ("Verdana",10))
        PStatus_label.grid(row = 8,column = 2,sticky = 'w')
        
        Sensor_1_canvas = FigureCanvasTkAgg(f_1, self)
        Sensor_1_canvas.draw()
        Sensor_1_canvas.get_tk_widget().grid(row = 5,column = 0)
        Sensor_2_canvas = FigureCanvasTkAgg(f_2, self)
        Sensor_2_canvas.draw()
        Sensor_2_canvas.get_tk_widget().grid(row = 5,column = 1)
        Sensor_difference_canvas = FigureCanvasTkAgg(f_3, self)
        Sensor_difference_canvas.draw()
        Sensor_difference_canvas.get_tk_widget().grid(row = 5,column = 2)
        
        
        ON = tk.Button(self, text="Turn ON",
                            command=lambda: ONOFF_ref.set('Y'),fg = 'green')
        ON.grid(row = 6,column = 2,sticky = 'w')
        OFF = tk.Button(self, text="Turn OFF",
                            command=lambda: ONOFF_ref.set('N'),fg = 'red')
        OFF.grid(row = 7,column = 2,sticky = 'w')
        button2 = tk.Button(self, text="Go To Street Condition",
                            command=lambda: controller.show_frame(Page1), font= ("Verdana",10))
        button2.grid(row = 10,columnspan = 3)
        
        
#-------------------------------------------------------------------------------------------------------------------------------------       
app = PipeChecking()
ani_1 = animation.FuncAnimation(f_1, animate, interval=15000)
ani_2 = animation.FuncAnimation(f_2, animate, interval=15000)
ani_3 = animation.FuncAnimation(f_3, animate, interval=15000)
ani_4 = animation.FuncAnimation(f_Temp, animate, interval=15000)
ani_6 = animation.FuncAnimation(f_HU, animate, interval=15000)
ani_7 = animation.FuncAnimation(f_AQ, animate, interval=15000)
ani = animation.FuncAnimation(f_1, animate1, interval=2000)
app.mainloop()
    