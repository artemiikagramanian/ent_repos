import RPi.GPIO as GPIO
import time 

def bin_10 (value):
    return list(map(int, bin(value)[2:].zfill(8)))

dac = [26, 19, 13, 6, 5, 11, 9, 10]
levels = 2**len(dac)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period = int(input())
    ch = ((2*levels)/period)
    while True:
        for i in range(256):
            GPIO.output(dac, bin_10(i))
            time.sleep(1/ch)
        for i in range(255, -1, -1):
            GPIO.output(dac, bin_10(i))
            time.sleep(1/ch)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()