# Rotary encoder gives the values of two connections, A (or CLK) and B (or DT).
# Depending on the direction it is being moved, the values will change in a
# cetrtain order.
#
# To set this up, connect + to 3.3v, GND to GND.
# Connect CLK to any pin and update variable ROTARY_A to it.
# Connect DT to any pin and update variable ROTARY_B to it.
# In addition, the knob itself can be pressed.
# Connect SW to any pin and update variable ROTARY_SW.

# Reference -
# http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/keyes-ky-040-arduino-rotary-encoder-user-manual/

import RPi.GPIO as GPIO
import time

ROTARY_A = 17
ROTARY_B = 19
ROTARY_SW = 21

class Rotary(object):
  def __init__(self):
    self._state = None
    self._value = 0

  def _button_event(self, unused_channel):
    print('Button state: {}'.format(GPIO.input(ROTARY_SW)))

  def _read_and_display(self, unused_channel):
    resultA = GPIO.input(ROTARY_A)  # GPIO.HIGH or GPIO.LOW
    resultB = GPIO.input(ROTARY_B)  # GPIO.HIGH or GPIO.LOW
    new_state = (resultA, resultB)
    if new_state != self._state:
      print(new_state, end=', ')
      # For clockwise, the states change like below -
      # (0, 1) - (0, 0) - (1, 0) - (1, 1) - (0, 1)
      # For anticlockwise, it is reverse.
      # Let's encode the states as 3 - 0 - 1 - 2 - 3.
      encode = lambda s: 3 if s == (0, 1) else s[0] + s[1]

      if self._state is not None:
        prev = encode(self._state)
        now = encode(new_state)
        delta = (now - prev) % 4
        if delta == 3:
          delta = -1
        self._value += delta
        print(self._value)

      self._state = new_state

  def main_loop(self):
    GPIO.setmode(GPIO.BCM)
    # Pull up - because by design, closing the circuit connects to GND.
    GPIO.setup(ROTARY_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(ROTARY_SW, GPIO.BOTH, callback=self._button_event)

    # # Option 1: Continuous polling.
    # while True:
    #   self._read_and_display()

    # Option 2: Handle events only.
    GPIO.add_event_detect(ROTARY_A, GPIO.BOTH, callback=self._read_and_display)
    GPIO.add_event_detect(ROTARY_B, GPIO.BOTH, callback=self._read_and_display)
    while True:
      time.sleep(1)

def main():
  print("Running...")
  rotary = Rotary()
  try:
    rotary.main_loop()
  finally:
    print("Cleaning up...")
    GPIO.cleanup()
  print("Done.")

if __name__ == "__main__":
  main()

