# Theory
# Connect: 5v --- Buzzer --- PNP transistor --- GND.
# Note that buzzer has a dedicated positive leg, which is larger.
# Then connect GPIO17 --- 1k ohm --- (.NP --- GND).

# As long as current is on in GPIO17, current cannot flow thru PNP.
# Setting GPIO17 to LOW allows current to flow thru the transistor.


# Similar circuit can work if we replace PNP with NPN -
# 5v --- Buzzer --- NPN --- GND.
# GPIO17 --- 1k ohm --- (.PN --- GND).
# But this time when there's no current, nothing happens; when there is
# current the buzzer buzzes.


import RPi.GPIO as GPIO
import time

LED_PIN = 17

def code():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN, GPIO.OUT)
  print("Low")
  GPIO.output(LED_PIN, GPIO.LOW)
  time.sleep(1)
  print("High")
  GPIO.output(LED_PIN, GPIO.HIGH)
  time.sleep(1)

def main():
  print("Running...")
  try:
    code()
  finally:
    print("Cleaning up...")
    GPIO.cleanup()
  print("Done.")

if __name__ == "__main__":
  main()

