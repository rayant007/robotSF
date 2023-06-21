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
    giraMotorL('L', 250, 150);
    giraMotorR('R', 250, 150);
}

void giraMotorL(char dir, int vel, int pulsos) {
    analogWrite(PWM, vel);
    if (dir == 'L') {
        while (contador<=pulsos)
        {
            digitalWrite(M1, LOW);
            digitalWrite(M2, HIGH);
            Serial.println(contador);
        }
        stopMotor();
        contador =0;
    }
}

void giraMotorR(char dir, int vel, int pulsos) {
    analogWrite(PWM, vel);
        while (contador<=pulsos)
        {
            digitalWrite(M1, HIGH);
            digitalWrite(M2, LOW);
            Serial.println(contador);
        }
        stopMotor();
        contador = 0;

}



void stopMotor() {
    analogWrite(PWM, 0);
    digitalWrite(M1, LOW);
    digitalWrite(M2, LOW);
}

void Contador() {
    contador++;
}