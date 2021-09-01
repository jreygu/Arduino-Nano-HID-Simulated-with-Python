const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int buttonPin3 = 4;
const int buttonPin4 = 5;
const int buttonPin5 = 6;
const int buttonPin6 = 7;
const int buttonPin7 = 8;
const int buttonPin8 = 9;
const int buttonPin9 = 10;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);
  pinMode(buttonPin8, INPUT);
  pinMode(buttonPin9, INPUT);
}

void loop() {
  if (digitalRead(buttonPin1) == HIGH) { Serial.print("a"); delay(500); } else {}
  if (digitalRead(buttonPin2) == HIGH) { Serial.print("b"); delay(500); } else {}
  if (digitalRead(buttonPin3) == HIGH) { Serial.print("c"); delay(500); } else {}
  if (digitalRead(buttonPin4) == HIGH) { Serial.print("d"); delay(500); } else {}
  if (digitalRead(buttonPin5) == HIGH) { Serial.print("e"); delay(500); } else {}
  if (digitalRead(buttonPin6) == HIGH) { Serial.print("f"); delay(500); } else {}
  if (digitalRead(buttonPin7) == HIGH) { Serial.print("g"); delay(500); } else {}
  if (digitalRead(buttonPin8) == HIGH) { Serial.print("h"); delay(500); } else {}
  if (digitalRead(buttonPin9) == HIGH) { Serial.print("i"); delay(500); } else {}

}
