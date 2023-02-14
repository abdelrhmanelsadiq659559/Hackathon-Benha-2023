//#include<Servo.h>
int ir1=8;
int ir2=9;
int count =0;

#define ledB 7
#define ledG 2
#define ledR 6

//Servo servo;
int angle=0;
int state=0;

void setup()
{
  Serial.begin(9600);
  pinMode(ir1,INPUT);
  pinMode(ir2,INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT); 
  pinMode(ledB, OUTPUT); 
  //servo.attach(10);
  //servo.write(90);

  
}
void loop()

{ 
  int value_ir1 = digitalRead(ir1);
  int value_ir2 = digitalRead(ir2);
  Serial.println("");
  Serial.print("Ir1 value=");
  Serial.print(value_ir1);
  Serial.println("");
  Serial.print("Ir2 value=");
  Serial.print(value_ir2);
  if (count ==0)
  {
    digitalWrite(ledR,HIGH);
    count++;
  }
  

  if(value_ir1==0)
  {
     digitalWrite(ledR,LOW);
     digitalWrite(ledB,HIGH);
     //analogWrite(ledG, HIGH);
     //analogWrite(ledB, LOW);
     //servo.write(0);
     delay(2000);
           
  }
  
  if(value_ir2==0)
  {

    //servo.write(90);
     digitalWrite(ledR,HIGH);
     digitalWrite(ledB,LOW);
     //analogWrite(ledG, LOW);
     //analogWrite(ledB, LOW);
     //servo.write(0);
     delay(2000);
  } 
}
