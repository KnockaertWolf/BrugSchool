"""Bestand met alle code voor het meten van het rekstrookje"""

import time
from qwiicscale import QwiicScale


class Rek:
    """Class voor alle functies voor het rekstrookje"""

    def __init__(self, file):
        self.file = file
        self.sensor = QwiicScale()
        self.start_time = 0
        self.times, self.straines = [], []

        self.offset = 1

    def begin(self):
        """Functie voor de setup"""
        self.start_time = time.time()
        self.sensor.begin()

    def calibrate(self):
        """Functie om de sensor te calibreren"""
        m1 = 1
        v1 = 4
        m2 = 5
        v2 = 20

        self.rico = (v2-v1)/(m2-m1)
        self.offset = v2 - self.rico*m2

    def calculate_strain(self, value):
        G = 9.81
        A = 30.1 * 98
        E = 70000
        massa = (value-self.offset)/self.rico
        kracht = massa * G

        strain = value # F/(A*E)
        return strain



    def read(self):
        """Functie om een meting uit te voeren"""
        with open(self.file, "w", encoding="utf-8") as f:
            value = self.calculate_strain(self.sensor.getReading())
            timestamp = time.time() - self.start_time

            strain = value

            self.times.append(timestamp)
            self.straines.append(strain)

            f.write(f"{timestamp},{strain}")
            f.flush()

            print(f"Time: {timestamp} | Strain: {strain}")
