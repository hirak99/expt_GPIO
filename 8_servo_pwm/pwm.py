# Untested; but expeceted to work on a servo motor.
# Connect the motor through an optocoupler, especially if it requires voltage
# higher than 5v, or large amount of current to operate.
import RPi.GPIO as GPIO
import time

LED_PIN = 27

# Pulse width in ms.
SERVO_PULSE_WIDTH = 50

def ms_to_dutycycle(ms):
  return ms / SERVO_PULSE_WIDTH * 100

def code():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN, GPIO.OUT)
  p = GPIO.PWM(LED_PIN, SERVO_PULSE_WIDTH)
  p.start(ms_to_dutycycle(1.))
  for modulation in [0.5, 1.0, 1.5]:
    cycle = ms_to_dutycycle(modulation)
    print('Pulse: {}ms / {}ms, duty cycle: {}%'.format(
      modulation, SERVO_PULSE_WIDTH, cycle))
    p.ChangeDutyCycle(cycle)
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

