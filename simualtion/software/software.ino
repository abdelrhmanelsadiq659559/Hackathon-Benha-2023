#include<Servo.h>
int count = 0;
char c;
String id;
int ir1=12;
int ir2=10;
int led=13;
Servo servo;
int angle=0;
int state=0;
void setup()
{
  Serial.begin(9600);
  pinMode(ir1,INPUT);
  pinMode(ir2,INPUT);
  pinMode(led,OUTPUT);
  servo.attach(11);
  servo.write(0);
  Serial.println("Please scan your RFID TAG");
  
}
void loop()

{ 
  int value_IR1 = digitalRead(ir1);
  int value_IR2 = digitalRead(ir2);
  /*Serial.println("");
  Serial.print("Ir1 value=");
  Serial.print(value_IR1);
  Serial.println("");
  Serial.print("Ir2 value=");
  Serial.print(value_IR2);*/
  //
if(value_IR1==0)
  {
    
   while(Serial.available()>0)
   {
      c = Serial.read();
      count++;
      id += c;
      if(count == 12)  
       {
         Serial.print(id);
         //break;
     
      if(id=="AB123456789A")
        {
        Serial.println(":is Valid TAG");
        digitalWrite(13, HIGH);
        servo.write(90);
        }
        else
        {
          digitalWrite(13, LOW);
          Serial.println("Invalid TAG");
        }
     }
  }
  count = 0;
  id="";
  delay(1000);
  if(value_IR2==0)
  {
    digitalWrite(led,LOW);
    servo.write(0);
  } 
}

}
