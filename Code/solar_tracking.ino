#include <Servo.h>

const int LDR1_PIN = A0;   // LDR 1 connected to analog pin A0
const int LDR2_PIN = A1;   // LDR 2 connected to analog pin A1
const int SERVO_PIN = 9;   // Servo connected to digital pin 9

Servo myServo;

void setup() {
  Serial.begin(9600);       // Start serial communication for debugging
  myServo.attach(SERVO_PIN); // Attach servo motor to pin 9
  myServo.write(160);       // Start servo at 160 degrees to compensate for bias
}

void loop() {
  int ldr1Value = analogRead(LDR1_PIN);  // Read LDR 1 value
  int ldr2Value = analogRead(LDR2_PIN);  // Read LDR 2 value

  // Calculate the difference between LDR readings
  float difference = float(ldr2Value - ldr1Value);

  // Map the difference to servo angle range (0 to 180 degrees)
  int servoAngle = 110 + int(difference * 0.1); // Adjust offset for initial bias

  // Constrain the servo angle to 0 - 180 degrees
  servoAngle = constrain(servoAngle, 0, 180);

  // Move the servo to the calculated position with a doubled delay
  myServo.write(servoAngle);

  // Send LDR values and servo angle over serial
  Serial.print("LDR1:");
  Serial.print(ldr1Value);
  Serial.print(",LDR2:");
  Serial.print(ldr2Value);
  Serial.print(",Angle:");
  Serial.println(servoAngle);

  // Add a doubled delay between servo movements
  delay(1000); // Adjust delay time as needed
}
