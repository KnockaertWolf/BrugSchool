"""Bestand met alle code voor het controlleren van de brug"""

import RPi.GPIO as GPIO

class Brug:
    """Brug Controller"""

    def __init__(self, pin1, pin2):
        # 0 = close && 1 = open && 2 = nothing
        self.brug_state = 0
        self.up_pin = pin1
        self.down_pin = pin2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.up_pin, GPIO.OUT)
        GPIO.setup(self.down_pin, GPIO.OUT)

        GPIO.output(self.up_pin, GPIO.HIGH)
        GPIO.output(self.down_pin, GPIO.HIGH)

    def open(self, value):
        """Brug Open/Dicht"""
        if value == 1 and self.brug_state == 0:
            self.brug_state = 1
            
            GPIO.output(self.down_pin, GPIO.HIGH)
            GPIO.output(self.up_pin, GPIO.LOW)

        if value == 0 and self.brug_state == 1:
            self.brug_state = 0

            GPIO.output(self.up_pin, GPIO.HIGH)
            GPIO.output(self.down_pin, GPIO.LOW)


        print(f"Brug is nu: {'OPEN' if self.brug_state == 1 else 'DICHT'}")

    def cleanup(self):
        GPIO.cleanup()
