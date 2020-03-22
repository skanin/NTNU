#include<SoftwareSerial.h>
#include<PLabBTSerial.h>


const int btnPin = 2;
const int buzzerEn = 9; 
const int tx = 10;
const int rx = 11;

int count = 0;

PLabBTSerial btSerial(tx, rx);
String data;


char msg[100];
void updateBTSerial() {
  int availableCount = btSerial.available();
  if (availableCount > 0) {
    btSerial.read(msg, availableCount);
    char *divided = strchr(msg,',');
    int msgValue = 0;
    if (divided != 0) {
       divided[0] = 0; divided++;
       String str(divided);
       msgValue = str.toInt();
    };
    String msgString(msg);
    BTSerialMessageReceived(msgString, msgValue);   
  }
}

int buttonStateBtn;
void setup() {
  btSerial.begin(9600);
  Serial.begin(9600);
  Serial.println("Hello World");
  pinMode(btnPin, INPUT);
  pinMode(buzzerEn, OUTPUT);
}

void test(){
  tone(buzzerEn, 5000);
}
double hoursToMili(double hours){
  return hours * 3600000;
 }
 
void loop() {
  delay(hoursToMili(8));
   while(count <= 1000){
    for(int i = 1000; i < 12000; i+=100){
      tone(buzzerEn, i);
      delay(10);
      updateBTSerial();
    }
    noTone(buzzerEn);
  }
  noTone(buzzerEn);
}

void BTSerialMessageReceived(String msgString, int msgValue) {
  Serial.println("Message: " + msgString);
  if(msgString == "klikk") {
    count++;
    Serial.println(count);
  }
}


