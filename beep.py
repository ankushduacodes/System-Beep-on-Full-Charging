import os
import beepy
import psutil

def main():
    sound_played = False
    while (True):
        battery = psutil.sensors_battery()
        if (battery.power_plugged and battery.percent == 100 and not sound_played):
            beepy.beep(sound=1)
            sound_played = True
            return

if __name__ == "__main__":
    main()
