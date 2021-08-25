#import gpiozero as gp
import time

class Pump(object):
    """class to define the pump object"""

    pin = 17
    pump_rate = 0


    #gpio_pin = gp.DigitalOutputDevice(pin = pin)

    # constructor
    def __init__(self, pin, pump_rate):
        self.pin = pin
        self.pump_rate = pump_rate

        return

    def run(pump_time):
        ''' runs the pump for specified amount of time 
            in seconds '''

        # turn output pin on
       # gpio_pin.on()

        # wait for the time to pass
        time.sleep(pump_time)

        # turn pump off
        #gpio_pin.off()

        return


