void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available() && Serial.read() == 'H'){
    digitalWrite(13, HIGH);
  }
  
  if(Serial.available() && Serial.read() == 'L'){
    digitalWrite(13, LOW);
  }
  
  
}
