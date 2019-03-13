char inByte;
bool off = true;
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Ready");
}

void loop() {
  if (Serial.available() > 0) { // only send data back if data has been sent
    inByte = Serial.read(); // read the incoming data
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line
    if(inByte == '0'){
      off = true;
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
    }
    else if(inByte == '1'){
      off = false;
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
    }
  }
  else{
    if(off == false){
      digitalWrite(LED_BUILTIN, LOW);  
      delay(1000);
      // turn the LED off by making the voltage LOW
    }
    else if(off == true){
       digitalWrite(LED_BUILTIN, HIGH); 
       delay(1000); 
    }
    delay(100);
  }
}
