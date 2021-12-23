import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("servo wave")


def pulse(pin_nr, high_time, low_time):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)


def servo_pulse(pin_nr, position):
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """
    if position > 100:
        position = 100
    elif position < 0:
        position = 0

    pulsetime = ((position * 0.02) + 0.5)/1000
    # DEBUG SHIT print(f"{pin_nr}; {pulsetime}; 0.02 --- {position}")
    pulse(pin_nr, pulsetime, 0.020)




servo = 18
GPIO.setup(servo, GPIO.OUT)
while True:
    for i in range(0, 100, 1):
        servo_pulse(servo, i)
    for i in range(100, 0, -1):
        servo_pulse(servo, i)
