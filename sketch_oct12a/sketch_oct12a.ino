#include "WiFi.h"
#include <HTTPClient.h>

int inPinTermo = 2; 
int inPinMovement = 3;

int inPinTouch[] = {5,6,7,8,9,10,11,12};
int inPinDropletAnalog = A0;

int valTermo = -1;      
int valMovement = -1;
int valDropletAnalog = -1;
int touchVals[] = {0,0,0,0,0,0,0,0};

String serverName = "http://192.168.0.105:8000/uploadData";


void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin("TP-Link_C79B", "36060368");
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(9600);
  pinMode(inPinTermo, INPUT);
  pinMode(inPinMovement, INPUT);
  pinMode(inPinDropletAnalog, INPUT); 
  

  for (int i = 0; i < 8; i++) {
    pinMode(inPinTouch[i], INPUT); 
  }

  initWiFi();
}

void loop() {
  HTTPClient http;
  valTermo = digitalRead(inPinTermo);
  valMovement = digitalRead(inPinMovement);

  for (int i = 0; i < 8; i++) {
    touchVals[i] = digitalRead(inPinTouch[i]); 
  }

  valDropletAnalog = analogRead(inPinDropletAnalog);

  Serial.print(valTermo);
  Serial.print(",");
  Serial.print(valMovement);
  Serial.print(",");
  Serial.print(valDropletAnalog);
  Serial.print(",");

  for (int i = 0; i < 8; i++) {
    Serial.print(touchVals[i]);
    Serial.print(",");
  }

    // Your Domain name with URL path or IP address with path
  http.begin(serverName.c_str());
  http.addHeader("Content-Type", "application/json");
  String data = "{\"temperature\":";
  data += valTermo;
  data += ", \"movement\":"; 
  data += valMovement;
  data += ", \"humidity\":";
  data += valDropletAnalog;
  data += "}";
  int httpResponseCode = http.POST(data);

  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();

  delay(1000);
}