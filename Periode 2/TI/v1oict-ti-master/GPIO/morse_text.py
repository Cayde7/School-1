import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse text" )

def pulse( pin_nr, high_time, low_time ):
   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(low_time)

def morse( pin_nr, dot_length, text ):
   for each in text:
      if each == '.':
         pulse(pin_nr, dot_length, dot_length)
      elif each == '-':
         pulse(pin_nr, dot_length * 2, dot_length)
      else:
         pulse(pin_nr, 0, dot_length)

def morse_text( pin_nr, dot_length, text ):
   """
   Laat de string s horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: lowercase letters, spatie.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   # https://www.geeksforgeeks.org/morse-code-translator-python/ DICT geleent van de URL
   MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
                      ' ': ' '}
   output = ''
   for each in text:
      output += MORSE_CODE_DICT[each.capitalize()]
   morse(pin_nr, dot_length, output)
   return

led = 18
GPIO.setup( led, GPIO.OUT )
morse_text( led, 0.2, "Hello world" )
