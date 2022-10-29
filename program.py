# pip3 install screen-brightness-control
import screen_brightness_control as sbc
# pip3 install
import keyboard
# exists by default
from time import sleep

# pip3 install pycaw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# pip3 install ctypes
from ctypes import cast, POINTER
# pip3 install comtypes
from comtypes import CLSCTX_ALL

# Also important to install:
#   pip install pythonw

# To run this program in the background just execute the command:
#   pythonw program.py
# And to make it capable of outputting any errors and outputs write the command like this:
#   pythonw program.py 1>stdout.txt 2>stderr.txt

# create a device to control sound of the system
devices = AudioUtilities.GetSpeakers()
# create and interface to activate the device
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
# cast the device to point to the system default sound
volume = cast(interface, POINTER(IAudioEndpointVolume))
# currentVolume = volume.GetMasterVolumeLevel()
# print(volume.GetMasterVolumeLevel())
# Define MasterVolumeLevel values for every 5 bits of volume
volumeLevels = {0: -96,
                5: -45.02272033691406,
                10: -34.75468063354492,
                15: -28.681884765625,
                20: -24.35443115234375,
                25: -20.989887237548828,
                30: -18.236774444580078,
                35: -15.906672477722168,
                40: -13.886737823486328,
                45: -12.10401439666748,
                50: -10.508596420288086,
                55: -9.064839363098145,
                60: -7.746397495269775,
                65: -6.5332441329956055,
                70: -5.409796714782715,
                75: -4.363698959350586,
                80: -3.384982109069824,
                85: -2.4654886722564697,
                90: -1.5984597206115723,
                95: -0.7782278060913086,
                100: 0}
currentVolume = 100
# Set starting MasterVolumeLevel
volume.SetMasterVolumeLevel(volumeLevels[100], None)

# get the current brightness of the screen
brightnessSTR = sbc.get_brightness()
# convert the current brightness from str to int to make it capable of changing
brightness = int(brightnessSTR[0])

# Start the loop tht checks for input
print("waiting for input")
while True:
    if keyboard.is_pressed('f7') and brightness > 0:
        print("Brightness decreased by 10")
        brightness -= 10
        sleep(0.2)
    elif keyboard.is_pressed('f8') and brightness < 100:
        print("Brightness increased by 10")
        brightness += 10
        sleep(0.2)
    if keyboard.is_pressed('f1'):
        print("Volume state changed")
        if volume.GetMute() == 1:
            volume.SetMute(0, None)
        else:
            volume.SetMute(1, None)
        sleep(0.5)
    if keyboard.is_pressed("f2"):
        print("Volume decreased")
        if currentVolume > 0:
            currentVolume -= 5
        sleep(0.2)
    elif keyboard.is_pressed("f3"):
        print("Volume increased")
        if currentVolume < 100:
            currentVolume += 5
        sleep(0.2)
    # Set the current brightness of the system
    volume.SetMasterVolumeLevel(volumeLevels[currentVolume], None)
    sbc.set_brightness(str(brightness))
