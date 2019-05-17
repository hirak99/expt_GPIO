import RPi.GPIO as GPIO
import time

LED_PIN = 17

def code():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN, GPIO.OUT)
  p = GPIO.PWM(LED_PIN, 1000)
  p.start(0)
  for i in range(0, 101, 10):
    print(i)
    p.ChangeDutyCycle(i)
    time.sleep(0.25)

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

