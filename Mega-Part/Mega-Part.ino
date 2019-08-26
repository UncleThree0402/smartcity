#include "Air_Quality_Sensor.h"

#include "DFRobot_RGBLCD.h"
#include "Seeed_BME280.h"
#include <Wire.h>
#include <Scheduler.h>
#if defined(ARDUINO_ARCH_SAMD) && (USB_PID == 0x8D21)
#define Serial SerialUSB
#endif
float Vsig;
int AQ;
int Temp;
float  pressure;
int Altitude;
int Humidity;
char input;
int r;
int b;
int g;
int t=0;

BME280 bme280;
AirQualitySensor sensor(A0);

void setup() {
  Scheduler.start(setup1, loop1);
  Scheduler.start(setup2, loop2);
  
  
}

void loop() 
{
   yield();
}

void setup1()
{
  pinMode(7,OUTPUT);
  Serial.begin(9600); 
}

void loop1()
{
 input = Serial.read();
   if(input == 'Y')
   {
    digitalWrite(7,LOW);
   }
   if(input == 'N')
   {
    digitalWrite(7,HIGH);
   }
   delay(1); 
}

void setup2()
{
  Serial.begin(9600);
  if(!bme280.init()){
    Serial.println("Device error!");
  }
}

void loop2()
{
   int sensorValue;
   long  sum=0;
   for(int i=0;i<1024;i++)
   {  
      sensorValue=analogRead(A0);
      sum=sensorValue+sum;
      delay(2);
   }   
  sum = sum >> 10;
  Vsig = sum*4980.0/1023.0;
  
  Temp = bme280.getTemperature();
  pressure = bme280.getPressure();
  Altitude = bme280.calcAltitude(pressure);
  Humidity = bme280.getHumidity();
  Serial.println(Temp);
  Serial.println(Altitude);
  Serial.println(Humidity);
  int quality = sensor.slope();

  AQ = sensor.getValue();
  Serial.println(AQ);
  
  if (quality == AirQualitySensor::FORCE_SIGNAL) {
    Serial.println(3);
  }
  else if (quality == AirQualitySensor::HIGH_POLLUTION) {
    Serial.println(2);
  }
  else if (quality == AirQualitySensor::LOW_POLLUTION) {
    Serial.println(1);
  }
  else if (quality == AirQualitySensor::FRESH_AIR) {
    Serial.println(0);
  }
  if (Vsig < 50) {
    Serial.println(0);
  }
  if (Vsig > 50 && Vsig < 227) {
    Serial.println(1);
  }
  if (Vsig > 227 && Vsig < 318) {
    Serial.println(2);
  }
  if (Vsig > 318 && Vsig < 408) {
    Serial.println(3);
  }
  if (Vsig > 408 && Vsig < 503) {
    Serial.println(4);
  }
  if (Vsig > 503 && Vsig < 606) {
    Serial.println(5);
  if (Vsig > 606 && Vsig < 696) {
    Serial.println(6);
  }
  if (Vsig > 696 && Vsig < 795) {
    Serial.println(7);
  }
  if (Vsig > 795 && Vsig < 881) {
    Serial.println(8);
  }
  if (Vsig > 881 && Vsig < 976) {
    Serial.println(9);
  }
  if (Vsig > 976 && Vsig < 1079) {
    Serial.println(10);
  }
  if (Vsig > 1079 && Vsig < 1170) {
    Serial.println(11);
  }
  if (Vsig > 1170) {
    Serial.println(12);
  }

  delay(1000);
}
}
