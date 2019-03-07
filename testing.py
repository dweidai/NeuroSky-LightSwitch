from NeuroPy.NeuroPy import NeuroPy
import keyboard
#import serial
import time

#port = '/dev/cu.Dwei-WirelessiAP'
#port = '/dev/tty.Dwei-WirelessiAP'
#port = '/dev/tty.usbmodem1411'
print("program started")
#f = open("testfile.txt", "w")
#ard = serial.Serial(port,9600,timeout=5)
#ard = serial.Serial('/dev/tty.usbserial', 9600)
headset = None
print(headset)
headset = NeuroPy("/dev/cu.MindWaveMobile-SerialPo", 57600)
print(headset)
print("heatset initialized")
headset.start()
print("headset started")
'''headset.stop()
print(headset)
print("headset closed")
'''
while True:
    print("Attention: ", headset.attention)
    print("Meditation: ", headset.meditation)

    try:
        if keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        print("\t!!!!\nquit program\n\t!!!!!!\n")
        break  # if user pressed a key other than the given key the loop will break

headset.stop()
print(headset)
print("headset closed")

'''
headset.close()
while True:
    print("Attention: ", headset.attention)
    print("Meditation: ", headset.meditation)
    time.sleep(0.1)
'''

#call start method
'''confirm_meditate = 0
confirm_attention = 0
nb = input('To quit, press spacebar')

time.sleep(1)
while True:
    ard.flush()
    if keyboard_is_pressed('0'):
        ard.write("0")
        f.write("0 ")
        time.sleep(0.1)
    elif keyboard_is_pressed('1'):
        ard.write("1")
        f.write("1 ")
        time.sleep(0.1)
    try:
        if keyboard.is_pressed('q'):
            ard.write("0")
            f.write("SESSION ENDED")
            time.sleep(0.1)
            break
        else:
            pass
    except:
        ard.write("0")
        f.write("Quit UNEXPECTED")
        time.sleep(0.1)
        print("\t!!!!\nIncorrect input, quit unexpected\n\t!!!!!!\n")
        break  # if user pressed a key other than the given key the loop will break
    '''


