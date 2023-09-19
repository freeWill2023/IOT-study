
#include <Servo.h>

#define MAX 180
#define MIN 0
#define STEP 3

Servo servo;

int pos = 90;

void setup() {
  Serial.begin(9600);
  Serial.println("Control Servo by Serial");
  servo.attach(9);
  servo.write(pos);
  delay(15);
}

void loop() {
  if(Serial.available() > 0) {
    char ch = Serial.read();
    if(ch == '.'){
      if(pos + STEP <= MAX) pos = pos + STEP;
      else pos = MAX;
    }
    else if(ch == ','){
      if(pos - STEP >= MIN) pos = pos - STEP;
      else pos = MIN;
    }
    else if(ch == '1')  pos = 45;
    else if(ch == '2')  pos = 90;
    else if(ch == '3')  pos = 135;
    else;
    Serial.print("pos = ");
    Serial.println(pos);
    servo.write(pos);
    delay(15);
    }
  }
