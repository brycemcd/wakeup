import RPi.GPIO as GPIO
import time

light_gpio_pins = [17, 24, 27]

def turn_on(gpio_pin):
  GPIO.output(gpio_pin, GPIO.HIGH)

def turn_on_all_lights():
  for gpiopin in light_gpio_pins:
    turn_on(gpiopin)

def blink_all(times=3):
  delay = 0.1
  for n in range(times):
    turn_on_all_lights();
    time.sleep(delay);
    turn_off_all();
    time.sleep(delay);

def turn_off_all():
  for gpiopin in light_gpio_pins:
    GPIO.output(gpiopin, GPIO.LOW)

def arm_lights():
  for gpiopin in light_gpio_pins:
    GPIO.setup(gpiopin, GPIO.OUT)

def warn_light_on():
  turn_on(17)

def success_light_on():
  turn_on(24)

def error_light_on():
  turn_on(27)

def notify_beer():
  print("beer")
  warn_light_on();
  # make request here
  time.sleep(1);
  turn_off_all();
  success_light_on();
  time.sleep(1);
  turn_off_all();

def notify_whiskey():
  print("whiskey")
  warn_light_on();
  # make request here
  time.sleep(1);
  turn_off_all();
  error_light_on();
  time.sleep(1);
  turn_off_all();


def arm_button_actions():
  GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  while True:
    btn_2 = GPIO.input(22)
    btn_1 = GPIO.input(23)

    if (btn_1 == False):
      notify_beer()
      time.sleep(1)

    if (btn_2 == False):
      notify_whiskey()
      time.sleep(1)

## STOP FUNCTIONS, START PROCEDURE
GPIO.setmode(GPIO.BCM)

arm_lights()
blink_all()
arm_button_actions();
