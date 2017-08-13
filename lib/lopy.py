from machine import ADC

class LoPy(object):
    def __init__(self):
        self.adc = ADC()
        self.batt = self.adc.channel(attn=1, pin='P16')

    def get_batt(self):
        voltage = self.batt.value()
        voltage = voltage*3*1400/4095/1000
        # print("Battery V = %.3f" % voltage )
        return voltage
