import RPi.GPIO as GPIO
import time

def blink():
  print "LED on"
  GPIO.output(18,GPIO.HIGH)
  time.sleep(0.1)
  print "LED off"
  GPIO.output(18,GPIO.LOW)
  time.sleep(0.1)

def turn_on():
  print "LED on"
  GPIO.output(18,GPIO.HIGH)

def turn_off():
  print "LED off"
  GPIO.output(18,GPIO.LOW)

def blink_n_times(n):
  for itr in range(n):
    blink()
    time.sleep(0.05)
  
def button_loop():
  blink_n_times(3)
  while True:
    input_state = GPIO.input(4)
    if input_state == False:
      print('Button Pressed')
      blink_n_times(100)
      time.sleep(0.5)
      
def blink_funny():
  for itr in range(100):
    blink()
    time.sleep(0.05)
  
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# turn_on()
# turn_off()
# blink_funny()
button_loop()

# button_loop()


