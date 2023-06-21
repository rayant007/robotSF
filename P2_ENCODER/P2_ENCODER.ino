#define M1 9
#define M2 10
#define PWM 11
#define Encoder 2
int contador = 0;

void setup() {
  Serial.begin(9600);
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(Encoder, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(Encoder), contar, CHANGE);
}

void loop() {
  girarMotor("D", 255, 300);
  girarMotor("I", 150, 100);
  girarMotor("d", 100, 200);
}

void girarMotor(char dir, int vel, int pulsos) {
  analogWrite(PWM, vel);
  if (dir == "D" || dir == "d") {
    while (contador <= pulsos) {
      digitalWrite(M1, LOW);
      digitalWrite(M2, HIGH);
    }
    stopMotor();
  } else if (dir == "I" || dir == "i") {
    while (contador <= pulsos) {
      digitalWrite(M1, HIGH);
      digitalWrite(M2, LOW);
    }
    stopMotor();
  }
}

void contar() {
  contador++;
}

void stopMotor() {
  analogWrite(PWM, 0);
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
}