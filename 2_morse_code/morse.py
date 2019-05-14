import RPi.GPIO as GPIO
import time
import sys

LED_PIN = 17
BEAT = 0.125

class Morse(object):
  def __init__(self):
    self._lookup = self._get_codes()

  @staticmethod
  def _get_codes():
    # http://ascii-table.com/morse-code.php
    # Space between characters is already 3 units.
    # Space between words (' ') is two more units (total 5 units).
    lookup = {' ': '00'}
    for line in open('morsecode_lookup.txt'):
      line = line.strip().replace(' ', '')
      if not line:
        # Skip empty lines.
        continue
      code = line[1:].replace('.', '10').replace('-', '1110')
      lookup[line[0]] = code
    return lookup

  def _letter_to_morse(self, letter):
    return self._lookup[letter.upper()]

  def to_sequence(self, letters):
    code = []
    for i, letter in enumerate(letters):
      if i != 0:
        code.append(('', '000'))
      code.append((letter, self._letter_to_morse(letter)))
    return code

def morse_led(letters):
  morse_encoder = Morse()
  encoded = morse_encoder.to_sequence(letters)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN, GPIO.OUT)
  for letter, sequence in encoded:
    print(letter, end='', flush=True)
    for state in sequence:
      if state == "0":
        GPIO.output(LED_PIN, GPIO.HIGH)
      elif state == "1":
        GPIO.output(LED_PIN, GPIO.LOW)
      else:
        raise RuntimeError("Unknown character in seq.")
      time.sleep(BEAT)
  print()

def main():
  print("Running...")
  if len(sys.argv) > 1:
    to_encode = ' '.join(sys.argv[1:])
  else:
    to_encode = 'Hello world.'
  try:
    morse_led(to_encode)
  finally:
    print("Cleaning up...")
    GPIO.cleanup()
  print("Done.")

if __name__ == "__main__":
  main()

