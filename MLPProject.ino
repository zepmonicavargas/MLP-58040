#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 columns and 2 rows

const int capturePin = 7; // Pin for capture button
bool liveFeedActive = true; // State variable for live feed
unsigned long captureTime = 0; // Timestamp for capture event
bool showCaptureMessage = false; // Flag to indicate capture message display
String currentObject = ""; // Variable to store the current detected object
String currentPrice = ""; // Variable to store the current price

void setup()
{
  Serial.begin(9600);
  pinMode(8, OUTPUT);    // First LED (Arduino detected)
  pinMode(9, OUTPUT);    // Second LED (Breadboard detected)
  pinMode(10, OUTPUT);   // Third LED (Infrared Remote Control detected)
  pinMode(capturePin, INPUT_PULLUP); // Set capture button pin as input with internal pull-up resistor
  lcd.init();            // Initialize LCD
  lcd.backlight();       // Turn on backlight
}

void loop()
{
  // Read the state of the capture button
  int captureButtonState = digitalRead(capturePin);

  // If capture button is pressed, toggle liveFeedActive and send 'P' to Python code
  if (captureButtonState == LOW)
  {
    // Debounce the button
    delay(50);
    if (digitalRead(capturePin) == LOW)
    {
      liveFeedActive = !liveFeedActive; // Toggle live feed state
      Serial.write('P');
      if (!liveFeedActive)
      {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Captured          ");
        captureTime = millis(); // Record the time of capture
        showCaptureMessage = true;
      }
      else
      {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Live Feed Active  ");
      }
      delay(500); // Delay to debounce the button
    }
  }

  // Check if 3 seconds have passed since capture
  if (showCaptureMessage && (millis() - captureTime >= 2000))
  {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(currentObject);
    lcd.setCursor(0, 1);
    lcd.print(currentPrice);
    showCaptureMessage = false;
  }

  if (Serial.available() > 0)
  {
    char data = Serial.read();

    if (data == 'A')
    {
      digitalWrite(8, HIGH); // Turn on first LED (Arduino detected)
      digitalWrite(9, LOW);
      digitalWrite(10, LOW);
      currentObject = "Small";
      currentPrice = "Price: 500";
      if (!showCaptureMessage) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(currentObject);
        lcd.setCursor(0, 1);
        lcd.print(currentPrice);
      }
    }
    else if (data == 'B')
    {
      digitalWrite(8, LOW);
      digitalWrite(9, HIGH); // Turn on second LED (Breadboard detected)
      digitalWrite(10, LOW);
      currentObject = "Medium";
      currentPrice = "Price: 1000";
      if (!showCaptureMessage) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(currentObject);
        lcd.setCursor(0, 1);
        lcd.print(currentPrice);
      }
    }
    else if (data == 'C')
    {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      digitalWrite(10, HIGH); // Turn on third LED (Infrared Remote Control detected)
      currentObject = "Large";
      currentPrice = "Price: 1500";
      if (!showCaptureMessage) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(currentObject);
        lcd.setCursor(0, 1);
        lcd.print(currentPrice);
      }
    }
    else if (data == 'D')
    {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      digitalWrite(10, LOW); // Turn off all LEDs
      if (!showCaptureMessage) {
        lcd.clear();
      }
    }
  }
}
