#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int sensor_pin = PA0;   // Signal from the capacitive soil moisture sensor
int output_value;       // Value of soil moisture
int pump = PA1;         // Digital pin where the relay is plugged in
int threshold = 5;      // Threshold value to trigger the pump

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.clear();
  pinMode(sensor_pin, INPUT_ANALOG);
  pinMode(pump, OUTPUT);
  digitalWrite(pump, HIGH);
  delay(1000);
  lcd.setCursor(0, 0);
  lcd.print("IRRIGATION");
  lcd.setCursor(0, 1);
  lcd.print("SYSTEM IS ON ");
  lcd.print("");
  delay(3000);
  lcd.clear();
}

void loop() {
  output_value = analogRead(sensor_pin);
  output_value = map(output_value, 550, 0, 0, 100);

  Serial.print("Moisture : ");
  Serial.print(output_value);
  Serial.println("%");
  delay(1000);

  if (output_value < threshold) {
    digitalWrite(pump, LOW);
    lcd.setCursor(0, 0);
    lcd.print("Water Pump is ON ");
    lcd.setCursor(0, 1);
    lcd.print("Moisture : LOW ");
  } else {
    digitalWrite(pump, HIGH);
    lcd.setCursor(0, 0);
    lcd.print("Water Pump is OFF");
    lcd.setCursor(0, 1);
    lcd.print("Moisture : HIGH ");
  }
}
