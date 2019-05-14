# For this, connect the LED as in experiment 1. Then connect a button with one
# end to GND, and the other end to IN_PIN. No resistor is required for the
# button but it will use the PULL-UP resistance operated by the software.
import RPi.GPIO as GPIO
import time

IN_PIN = 16
OUT_PIN = 17

def code():
  GPIO.setmode(GPIO.BCM)
  # Creates a pull-up connection. This inserts a 10k ohm resistor to the input
  # pin and positive voltage. The other end must be connected to GND.
  # When the circuit is open, there's a small current flow with +ve voltage.
  # When the circuit is closed, it is equivalent to ground with 0 volt.
  GPIO.setup(IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  # Setup the putput pin.
  GPIO.setup(OUT_PIN, GPIO.OUT)

  # # Below is a polling based way of scanning the button.
  # while True:
  #   result = GPIO.input(IN_PIN)  # GPIO.HIGH or GPIO.LOW
  #   GPIO.output(OUT_PIN, result)
  #   time.sleep(0.01)

  # # Below is an interrupt based scanning of the button.
  while True:
    # Print dots (.) to indicate the loop.
    print(".", end='', flush=True)
    result = GPIO.input(IN_PIN)  # GPIO.HIGH or GPIO.LOW
    GPIO.output(OUT_PIN, result)
    # Note: While waiting, the system won't even respond to Ctrl+C.
    # Hence a small time is better.
    GPIO.wait_for_edge(IN_PIN, GPIO.BOTH, timeout=1000)  # Timeout is in ms.

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

