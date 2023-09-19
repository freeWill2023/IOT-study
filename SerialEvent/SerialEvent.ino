#include <Servo.h>
#include <stdlib.h>

Servo pan_servo;
Servo tilt_servo;

String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete
int pos_pan = 0;              // 0 ~ 180
int pos_tilt = 0;             // 0 ~ 180

void setup() {
  Serial.begin(9600);
  inputString.reserve(20);   // reserve 200 bytes for the inputString:
  
  pan_servo.attach(9);
  tilt_servo.attach(10);
}

void loop() {
  if (stringComplete) {

    if (inputString.substring(0, 3)=="pan")
    {
      pos_pan = atoi(inputString.substring(3).c_str()); //atoi: char* ==> int 형변환 , c_str(): string ==> char*로 변환
      Serial.println(pos_pan);
      pan_servo.write(pos_pan);
    }
    else if (inputString.substring(0, 4)=="tilt")
    {
      pos_tilt = atoi(inputString.substring(4).c_str()); //atoi: char* ==> int 형변환 , c_str(): string ==> char*로 변환
      Serial.println(pos_tilt);
      tilt_servo.write(pos_tilt);
    }
    else;
    
    inputString = "";        // clear the string:
    stringComplete = false;
  }
}

void serialEvent() {                   // serial 수신 event발생시 마다 실행  
  while (Serial.available()) {

    char inChar = (char)Serial.read();

    inputString = inputString + inChar;

    if (inChar == '\n') {              // inchar에 serial monitor로 '엔터'(\n)가 입력되면...
      stringComplete = true;
    }
  }
}
