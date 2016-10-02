import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)

# strat
pwm.start(90)
time.sleep(2)
print "servo moter start"

def update(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(.5)
    print "ChangeDutyCycle(%s)" % duty

try:
	while True:
		update(45)
		update(90)

except KeyboardInterrupt:
	print "GPIO closeed."
        pass

# stop
pwm.stop()
GPIO.cleanup()

