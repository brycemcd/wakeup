import RPi.GPIO as GPIO
import time

light_gpio_pins = [17, 27, 22, 23]

def turn_on(gpio_pin):
  print "LED on"
  GPIO.output(gpio_pin, GPIO.HIGH)

def turn_all_off():
  print "LED off"
  for gpiopin in light_gpio_pins:
    GPIO.output(gpiopin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

def gpio_lights():
  for gpiopin in light_gpio_pins:
    GPIO.setup(gpiopin, GPIO.OUT)
    turn_on(gpiopin)

  time.sleep(1000)
  turn_all_off()

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def button_state():
  while True:
    input_state_22 = GPIO.input(22)
    print('22: %', input_state_22)
    input_state_23 = GPIO.input(23)
    print('23: %', input_state_23)
    time.sleep(0.5)
    # if ((input_state_22 == False) or (input_state_23 == False):

button_state();
