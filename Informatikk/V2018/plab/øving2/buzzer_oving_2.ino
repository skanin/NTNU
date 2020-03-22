const int buzzer = 9;
const int btn = 2;
const int echo = 7;
const int trig = 6;

const int xAxis = A0;
const int yAxis = A1;
const int mouseButton = 12;
int xPos = 0;
int yPos = 0;
int buttonState = 0;

int buttonStateBtn = 0;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(buzzer, OUTPUT);
  pinMode(btn, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(xAxis, INPUT);
  pinMode(yAxis, INPUT);
  pinMode(mouseButton, INPUT_PULLUP);
}

void loop() {
  xPos = analogRead(xAxis);
  yPos = analogRead(yAxis);
  buttonState = digitalRead(mouseButton);

  Serial.print("X: ");
  Serial.print(xPos);
  Serial.print(" | Y: ");
  Serial.print(yPos);
  Serial.print(" | Button: ");
  Serial.println(buttonState);

  delay(100); 

  Serial.print("X: ");
  Serial.print(xPos);
  Serial.print(" | Y: ");
  Serial.print(yPos);
  Serial.print(" | Button: ");
  Serial.println(buttonState);

  if(buttonState == 1 && xPos != 0){
    tone(buzzer, xPos * 10);
  }else if(xPos == 0 && buttonState == 1 && yPos != 0){
    tone(buzzer, yPos * 10);
  }else if(yPos == 0 && xPos == 0){
    noTone(buzzer);
  }
  
  long duration, distance;
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance= duration*0.034/2;
  //Serial.println(distance);
  if(distance < 10 || distance > 100){
    noTone(buzzer);
  }else{
    tone(buzzer, distance*100);
  }
  
  
  buttonStateBtn = digitalRead(btn); 
    if(buttonStateBtn == HIGH){
      for(int x = 1000; x < 16000; x+=100){
        tone(buzzer, x);
        delay(10);
        }       
      noTone(buzzer);
    }
}
