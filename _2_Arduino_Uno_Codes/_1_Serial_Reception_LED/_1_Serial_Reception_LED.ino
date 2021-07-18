// Arduino Uno
// Receives A ,Switches on LED on Pin13 for 2 seconds
// Rahul.S

// (c) www.xanthium.in 2021
// Tutorial - https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial


void setup()
{
  //An LED is Connected Pin12 
  pinMode(12,OUTPUT);  //Make Pin12 Output
  digitalWrite(12,LOW);//Make Pin12 OFF

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps 8N1

}

void loop()
{
  char RxedByte = 0;

 if (Serial.available()) 
    {
      
      RxedByte = Serial.read();    
       
      switch(RxedByte)
      {
        case 'A':  digitalWrite(12,HIGH);
                   delay(1000);
                   digitalWrite(12,LOW);
                   break;

        case 'B': //your code
                   break;
        default:
                   break;
      }//end of switch()
    }//endof if 
}
      

  
