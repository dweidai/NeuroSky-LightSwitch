char inByte;

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
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if(inByte == '1'){
      digitalWrite(LED_BUILTIN, HIGH);
    }
  }
  else{
    Serial.println("No input");
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(100);
  }
}
