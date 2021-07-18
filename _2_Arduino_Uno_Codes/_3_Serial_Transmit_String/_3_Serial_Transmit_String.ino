// Arduino Uno
// Transmits a string to PC 
// Rahul.S

// (c) www.xanthium.in 2021
// Tutorial - https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial


void setup()
{
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps 8N1

}

void loop()
{
  char TextToSend[] = " Hello From Arduino Uno";
  Serial.println(TextToSend); // sends a \n with text
  delay(1000);
}
      

  
