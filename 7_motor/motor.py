# For circuit diagram, see this doc -
# https://docs.google.com/document/d/1p9nEoiwvlAH3IMAiv1Eso_laps1Fr7dj__bmiGsssz4

import RPi.GPIO as GPIO
import time

OUT_PIN1 = 17
OUT_PIN2 = 27

def code():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(OUT_PIN1, GPIO.OUT)
  GPIO.setup(OUT_PIN2, GPIO.OUT)
  # Wait for some time before start...
  time.sleep(5)
  for config in ["10", "11", "01", "00"]:
    print("Applying output: " + config)
    pin1 = int(config[0])
    pin2 = int(config[1])
    GPIO.output(OUT_PIN1, pin1)
    GPIO.output(OUT_PIN2, pin2)
    time.sleep(2)

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

