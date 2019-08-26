

#include <Scheduler.h>
#if defined(ARDUINO_ARCH_SAMD) && (USB_PID == 0x8D21)
#define Serial SerialUSB
#endif
volatile int Sensor_1;
volatile int Sensor_2;
int Calc_1;
int Calc_2;
int pin_sensor_1 = 2;
int pin_sensor_2 = 3;   
char userInput;  
void setup()
{
  Scheduler.start(setup1, loop1);
  Scheduler.start(setup2, loop2);
  Scheduler.start(setup3, loop3);
} 


void loop()
{
  yield();
}

void setup1() 
{ 
 pinMode(7, OUTPUT);

  
 Serial.begin(9600); 
  
} 

void loop1 ()    
{
  
    userInput = Serial.read();
   
    if(userInput == 'N')
    {
      digitalWrite(7,HIGH);
    }
    if(userInput == 'Y')
    {
      digitalWrite(7,LOW);
    }
  
    delay(1); 
}

void rpm_1 ()     
{ 
 Sensor_1++;


} 




 
void setup2() 
{ 
 pinMode(pin_sensor_1, INPUT);

  
 Serial.begin(9600); 
 

 attachInterrupt(0, rpm_1, RISING); 
 
} 

void loop2 ()    
{
 Sensor_1 = 0;      
 sei();            
 delay (1000);      
 cli();            
 Calc_1 = (Sensor_1 * 60 / 7.5); 
 


 Serial.println (Calc_1, DEC); 
  

}

void rpm_2 ()     
{ 
 Sensor_2++;


} 

void setup3() 
{ 
 pinMode(pin_sensor_2, INPUT);

  
 Serial.begin(9600); 
 

 attachInterrupt(1, rpm_2, RISING); 
 
} 

void loop3 ()    
{
 Sensor_2 = 0;      
 sei();            
 delay (1000);      
 cli();            
 Calc_2 = (Sensor_2 * 60 / 7.5); 
 


 Serial.println (Calc_2, DEC); 

}


 
 
