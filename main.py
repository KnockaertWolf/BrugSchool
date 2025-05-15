"""Mqtt code voor project"""

import time
import BlynkLib
import brug
import rek
from data import getDataToShow


BLYNK_AUTH = "t1oxQBosPKdaVGb8-xTRC_hXctVBJLrX"

blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud", port=443)
brug = brug.Brug(OMHOOGPIN, OMLAAGPIN)
# reksensor = rek.Rek("fig1.txt")


@blynk.on("V1")
def v1_event_handler(value):
    """Event handler for V1"""
    print(f"Blynk: {value}")
    brug.open(int(value[0]))

# reksensor.begin()
# reksensor.calibrate(30)


while True:
    blynk.run()

    xArray, yArray = getDataToShow("fig1.txt")
    try:
        if yArray:
            blynk.virtual_write(2, yArray[-1])
    except Exception as e:
        print(f"virtual_write failed: {e}")

    time.sleep(0.1)
    # reksensor.read()
