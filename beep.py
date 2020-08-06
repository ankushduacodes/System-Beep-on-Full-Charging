#!/usr/bin/python3
import os
import beepy
import psutil

def main():
    sound_played = False
    while (True):
        battery = psutil.sensors_battery()
        if (not battery.power_plugged or battery.percent != 100 and not sound_played):
            continue
        beepy.beep(sound=1)
        sound_played = True
        return

if __name__ == "__main__":
    main()
