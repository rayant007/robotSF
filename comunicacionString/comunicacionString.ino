

void setup() {
  Serial.begin(9600);
  int n = 0;
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  
  if (Serial.available()>0){
    int number = Serial.parseInt();
    n = number;
    Serial.print(number);
  }                     // wait for a second

  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(n); 

  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
  
  
}