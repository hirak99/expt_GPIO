import RPi.GPIO as GPIO
import time

LED_PIN = 17
SEQUENCE = "10100000"
BEAT = 0.125

def code():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN, GPIO.OUT)
  for _ in range(5):
    for state in SEQUENCE:
      to_set = GPIO.HIGH if state == "0" else GPIO.LOW
      GPIO.output(LED_PIN, int(to_set))
      time.sleep(BEAT)

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

