import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch = 23
switch2 = 4

toggle = 0

GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
while True:
   if GPIO.input(switch):
      toggle = 1
   if GPIO.input(switch2):
      toggle = 0

   if toggle:
      GPIO.output(led, GPIO.HIGH)
   else:
      GPIO.output( led, GPIO.LOW )
   time.sleep( 0.1 )
