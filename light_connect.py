#!/usr/bin/env python
# coding=utf-8

from lifxlan import LifxLAN
import sys

lifxlan = LifxLAN()

def set_power(state):
    lifxlan.set_power_all_lights(state, rapid=True)

if __name__ == "__main__":
    if sys.argv[1] == 'on':
        set_power('on')
    elif sys.argv[1] == 'off':
        set_power('off')
