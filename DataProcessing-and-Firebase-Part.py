import serial
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import time
from threading import Thread
import requests
#---------------------------------------FireBaseKeySetting----------------------------------

cred = credentials.Certificate("./teenscancode-caee5-firebase-adminsdk-ip0g2-e7d0d8e474.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://teenscancode-caee5.firebaseio.com'
})

#---------------------------------------DateList-----------------------------

num_1 = 2
num_2 = 6
datalist_1 = [0]*num_1
datalist_2 = [0]*num_2

#--------------------------------------FireBaseVarSetting-------------------------------------------

Sensor_1_ref = db.reference('Sensor_1')
Sensor_2_ref = db.reference('Sensor_2')
Difference_ref = db.reference('Difference')
ONOFF_ref = db.reference('ONOFF')
Temperature_ref = db.reference('Temperature')
Altitude_ref = db.reference('Altitude')
Humidity_ref = db.reference('Humidity')
AQ_ref = db.reference('AQ')
AQ_stat_ref = db.reference('AQ_stat')
UV_ref = db.reference('UV')


#---------------------------------------------ConnectionSetting--------------------------------------------------

Sensor_board = serial.Serial('COM3', 9600)
Sensor_board_1 = serial.Serial('COM4', 9600)

#---------------------------------------------DateProcessing(Collectiong))---------------------------------------------------------

while 1:
    
    for i in range(0,num_1):
        global data_1
        global data_2
        
        datalist_1[i] = Sensor_board.readline()
        data_1 = int(datalist_1[0])
        data_2 = int(datalist_1[1])
        Sensor_1_ref.set(data_1)
        Sensor_2_ref.set(data_2)
        Difference_ref.set(data_1 - data_2)
        
    for i in range(0,num_2):
        datalist_2[i] = Sensor_board_1.readline()
        Temperature = int(datalist_2[0])
        Altitude = int(datalist_2[1])
        Humidity = int(datalist_2[2])
        AQ = int(datalist_2[3])
        AQ_stat = int(datalist_2[4])
        UV =int(datalist_2[5])
        Temperature_ref.set(Temperature)
        AQ_ref.set(AQ)
        Altitude_ref.set(Altitude)
        Humidity_ref.set(Humidity)
        AQ_stat_ref.set(AQ_stat)
        UV_ref.set(UV)
        
        
        
#---------------------------------------------LeakSignal(OutPut)-----------------------------------
        
        if(ONOFF_ref.get() =='Y'):
            Sensor_board_1.write(b'Y')
        elif(ONOFF_ref.get() =='N'):
            Sensor_board_1.write(b'N')
        
#----------------------IFTTT-----------------------------------------
            
        if(data_1 - data_2 > 40):
            ONOFF_ref.set('N')
            requests.post("https://maker.ifttt.com/trigger/pipe/with/key/d1Yl0cCBf55n4CO26axRlW")
        
        
    
        
        
        
        
         



    
        
    
          
        



