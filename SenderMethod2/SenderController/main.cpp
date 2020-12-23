#include <Arduino.h>

void handleByte(char in);
void readByte();

void handle01();
void handle02();
void handle03();

void pulseOut(int pin);

const int I_1=13;
const int O_1=12;

const int I_2=11;
const int O_2=10;

const int I_3=9;
const int O_3=8;

void setup() {
    Serial.begin(115200);
    Serial.println("<Arduino is ready>");
    pinMode(I_1, INPUT);
    pinMode(I_2, INPUT);
    pinMode(I_3, INPUT);
    pinMode(O_1, OUTPUT);
    pinMode(O_2, OUTPUT);
    pinMode(O_3, OUTPUT);
    digitalWrite(O_1, LOW);
    digitalWrite(O_2, LOW);
    digitalWrite(O_3, LOW);

}

void loop() {
    readByte();
    
}

void handleByte(char in){
  switch (in)
  {
  case 0x01:
      Serial.println("Handle 0x01");
      handle01();
      break;
  case 0x02:
      Serial.println("Handle 0x02");
      handle02();
      break;
  case 0x03:
      Serial.println("Handle 0x03");
      handle03();
      break;
  default:
      break;
  }
}

void readByte() {
    char rc;
   
    if (Serial.available() > 0) {
        rc = Serial.read();
        handleByte(rc);
        delay(100);
    }
}

void pulseOut(int pin){
    digitalWrite(pin, HIGH);
    delayMicroseconds(100);
    digitalWrite(pin, LOW);
}

void handle01(){
    while (digitalRead(I_1) == LOW){
        delay(10);
    }
    pulseOut(O_1);
    while (digitalRead(I_1) == LOW){
        delay(10);
    }
    Serial.println("SEND O_1");
}

void handle02(){
    while (digitalRead(I_2) == LOW){
        delay(10);
    }
    pulseOut(O_2);
    while (digitalRead(I_2) == LOW){
        delay(10);
    }
    Serial.println("SEND O_2");
}

void handle03(){
    while (digitalRead(I_3) == LOW){
        delay(10);
    }
    pulseOut(O_3);
    while (digitalRead(I_3) == LOW){
        delay(10);
    }
    Serial.println("SEND O_3");
}
