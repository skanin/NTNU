#include <Servo.h>

const int buttonPin = 2;
const int redPinCar = 11;
const int yellowPinCar = 9;
const int greenPinCar = 8;

const int redPinHuman = 7;
const int greenPinHuman = 6;

//int buttonPushCounter = 0;
int pos = 0;
int buttonState = 0;

Servo myservo;

void setup() {
  Serial.begin(9600);
  pinMode(redPinCar, OUTPUT);
  pinMode(yellowPinCar, OUTPUT);
  pinMode(greenPinCar, OUTPUT);
  pinMode(greenPinHuman, OUTPUT);
  pinMode(redPinHuman, OUTPUT);
  pinMode(buttonPin, INPUT);
  myservo.attach(3);
  delay(50);
  myservo.write(45);
  delay(50);
  digitalWrite(greenPinCar, HIGH);
  digitalWrite(redPinHuman, HIGH);
}
 void click(){
    delay(1000);
    digitalWrite(redPinCar, LOW);
    digitalWrite(greenPinCar, LOW);
    digitalWrite(greenPinHuman, LOW);
    digitalWrite(redPinHuman, HIGH);
    digitalWrite(yellowPinCar, HIGH);
    delay(1000);
    digitalWrite(yellowPinCar, LOW);
    digitalWrite(redPinCar, HIGH);
    delay(2000);
    digitalWrite(redPinHuman, LOW);
    digitalWrite(greenPinHuman, HIGH);
    myservo.write(0);
    delay(50);
    delay(5000);
    digitalWrite(greenPinHuman, LOW);
    digitalWrite(redPinHuman, HIGH);
    myservo.write(45);
    delay(2000);
    digitalWrite(yellowPinCar, HIGH);
    delay(1000);
    digitalWrite(redPinCar, LOW);
    digitalWrite(yellowPinCar, LOW);
    digitalWrite(greenPinCar, HIGH);
  }

void loop() {
  buttonState = digitalRead(buttonPin); 
    if(buttonState == HIGH){
      Serial.print(myservo.attached());
      
      click();
    }
}

