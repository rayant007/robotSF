#define M1 9
#define M2 10
#define PWM 11
#define Encoder 2


int contador=0;


void setup() {
  Serial.begin(9600);
    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);
    pinMode(Encoder, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(Encoder), Contador, CHANGE);
}

void loop() {
    giraMotor('A', 255, 4600);
    giraMotor('R', 255, 4600);
    //giraMotor('R', 100, 600); gira en sentido horario 600 pulsos 3 vueltas aprox a una velocidad 100
    //giraMotor('a', 200, 200);
}

void giraMotor(char dir, int vel, int pulsos) {
    analogWrite(PWM, vel);
    if (dir == 'A'|| dir == 'a') {
        while (contador<=pulsos)
        {
            digitalWrite(M1, LOW);
            digitalWrite(M2, HIGH);
            Serial.println(contador);
        }
        stopMotor();
    }else if (dir == 'R'|| dir == 'r') {
        while (contador<=pulsos)
        {
            digitalWrite(M1, HIGH);
            digitalWrite(M2, LOW);
            Serial.println(contador);
        }
        stopMotor();
}

}

void stopMotor() {
    analogWrite(PWM, 0);
    digitalWrite(M1, LOW);
    digitalWrite(M2, LOW);
}

void Contador() {
    contador++;
}