int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
}

void loop() {
  // put your main code here, to run repeatedly:
  char input = ' ';
  if(Serial.available()){ // only send data back if data has been sent
    char input = Serial.read(); // read the incoming data
  }
  if(input == '0'){
    DigitalWrite(led, HIGH);
  }
  else if(input == '1'){
    DigitalWrite(led, LOW);
  }
}
