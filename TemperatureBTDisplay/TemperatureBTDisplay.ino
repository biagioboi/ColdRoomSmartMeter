#include "DHT.h"
#include <LiquidCrystal.h>
#define DHTPIN 12   
#define DHTTYPE DHT11
#include <SoftwareSerial.h>

SoftwareSerial BTserial(8, 9); // RX | TX

DHT dht(DHTPIN, DHTTYPE);

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 2, en = 3, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
    // set up lcd, dht and serial
    lcd.begin(16, 2);
    BTserial.begin(9600);
    dht.begin();
    Serial.begin(9600);
    
    // Print a message to the LCD.
    lcd.print("Curr. temp:");
}


void loop() {
  lcd.setCursor(0, 1);
  // read also the humidity but not used for the moment
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(t)) {
    lcd.print("err.            ");
    Serial.print("nan");
    return;
  }
  BTserial.println(t);
  lcd.print(t);
  Serial.println(t);
  lcd.print((char)223);
  lcd.print("C");
  delay(2000);
}
