#define M1 8
#define M2 9
#define PWM 10
#define Encoder 2  //permite contar pulsos
//MOTOR 2
#define M3 11
#define M4 12
#define PWM2 13
#define Encoder2 3  //permite contar pulsos

int contador=0;
int contador2=0;

void setup() {
  Serial.begin(9600);
    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);

    pinMode(M3, OUTPUT);
    pinMode(M4, OUTPUT);

    pinMode(Encoder, INPUT_PULLUP);  //pin 2
    pinMode(Encoder2, INPUT_PULLUP);  //pin 2

    attachInterrupt(digitalPinToInterrupt(Encoder), Contador, CHANGE);
    attachInterrupt(digitalPinToInterrupt(Encoder2), Contador2, CHANGE);
}
//8800 eje 1 vuelta completa
//4600 eje 2
//4390 1/4 vuelta eje 1
void loop() {
    giraMotor('A', 255, 1000);
    giraMotor2('B', 255, 1500);
}

void giraMotor(char dir, int vel, int pulsos) {
    analogWrite(PWM, vel);
    if (dir == 'A') {
          while (contador<=pulsos)
          {
            digitalWrite(M1, LOW);
            digitalWrite(M2, HIGH);
            Serial.println(contador);
          }
        stopMotor();
}
}

void giraMotor2(char dir, int vel, int pulsos) {
    analogWrite(PWM2, vel);
    if (dir == 'B') {
          while (contador2<=pulsos)
          {
            digitalWrite(M3, LOW);
            digitalWrite(M4, HIGH);
            Serial.println(contador2);
          }
        stopMotor();
}
}


void stopMotor() {
    analogWrite(PWM, 0);
    digitalWrite(M1, LOW);
    digitalWrite(M2, LOW);
    
    //motor2
    analogWrite(PWM2, 0);
    digitalWrite(M3, LOW);
    digitalWrite(M4, LOW);
    
}


void Contador() {
    contador++;
}

void Contador2(){
  contador2++;
}
