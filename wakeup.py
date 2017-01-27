import RPi.GPIO as GPIO
import time
import datetime

import os

# TODO: why does this get set to UTC when running as cron?
os.environ['TZ'] = 'America/New_York'

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

def current_datetime():
  return datetime.datetime.now()

def current_time():
  return datetime.datetime.now().timetz()

def min_wakeuptime():
  """Any hour before this hour is NOT okay to wakeup"""
  return datetime.time(07, 10)

def max_wakeuptime():
  """
  Any hour after this hour indicates that a child can not 
  possibly sleep this long
  """
  return datetime.time(20, 00)

def wakeup_ok():
  print(min_wakeuptime())
  print(max_wakeuptime())
  print(current_time())
  return (min_wakeuptime() < current_time() < max_wakeuptime())

def log_button_push():
  f = open('/home/pi/Desktop/button_log.csv', 'a')
  f.write( str(current_datetime()) + ',' + str(current_time()) + ',' + str(min_wakeuptime()) + ',' + str(max_wakeuptime()) + '\n')
  f.close()

def check_wakeup():
  log_button_push()
  warn_light_on()
  time.sleep(0.5)
  turn_off_all()

  if wakeup_ok():
    success_light_on();
  else:
    error_light_on();

  time.sleep(1.5);
  turn_off_all();

def arm_button_actions():
  GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  while True:
    btn_1 = GPIO.input(22)

    if (btn_1 == False):
      check_wakeup()
      time.sleep(1)

## STOP FUNCTIONS, START PROCEDURE
GPIO.setmode(GPIO.BCM)

arm_lights()
blink_all()
arm_button_actions();
