import collections
import json
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime

cred = credentials.Certificate("./teenscancode-caee5-firebase-adminsdk-ip0g2-e7d0d8e474.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://teenscancode-caee5.firebaseio.com'
})
#--------------------------------------------FireBaseSetup--------------------------------------------------------
Sensor_1_ref = db.reference('Sensor_1')
Sensor_2_ref = db.reference('Sensor_2')
Temperature_ref = db.reference('Temperature')
Altitude_ref = db.reference('Altitude')
Humidity_ref = db.reference('Humidity')
AQ_ref = db.reference('AQ')
AQ_stat_ref = db.reference('AQ_stat')
UV_ref = db.reference('UV')

#---------------------------------------------DateListSetup-----------------------------------------------------------------

a=[{"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()},
   {"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()},
   {"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()},
   {"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()},
   {"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()},
   ]

#----------------------------------------------jsonInput---------------------------------------------------
while True:
    a[:0]= [{"sensor_1":Sensor_1_ref.get(),"sensor_2":Sensor_2_ref.get(),"timestamp":int(round(time.time())+28800),"Temperature":Temperature_ref.get(),"Altitude":Altitude_ref.get(),"Humidity":Humidity_ref.get(),"AQ":AQ_ref.get(),"AQ_stat":AQ_stat_ref.get(),"UV":UV_ref.get()}]
    a.pop()
    print(a)
    with open("DATA.json",'w')as json_file:
        json.dump(a,json_file)
    time.sleep(15)
    
