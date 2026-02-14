#include <WiFi.h>
#include <HTTPClient.h>

const int flexPins[] = {A0, A1, A2, A3, D4}; // Pins on XIAO
int thresholds[] = {600, 600, 600, 600, 600};

void setup() {
  Serial.begin(115200);
  // WiFi connection logic here
}

void loop() {
  String pattern = "";
  for(int i=0; i<5; i++) {
    int val = analogRead(flexPins[i]);
    pattern += (val > thresholds[i]) ? "1" : "0";
    if(i < 4) pattern += ",";
  }

  // Only send if a gesture is detected (not 0,0,0,0,0)
  if(pattern != "0,0,0,0,0") {
    HTTPClient http;
    http.begin("http://your-speech-app.com/gesture");
    http.addHeader("Content-Type", "application/json");
    String json = "{\"pattern\":\"" + pattern + "\"}";
    http.POST(json);
    http.end();
  }
  
  delay(1000);
}
