from NeuroPy import NeuroPy
import keyboard
import serial

print("program started")
f = open("testfile.txt", "w")
ser = serial.Serial('/dev/tty.usbserial', 9600)

#call start method
confirm_meditate = 0
confirm_attention = 0
nb = input('To quit, press spacebar')
while True:
    if keyboard_is_pressed('0'):
        ser.write("0")
        f.write("0 ")
    elif keyboard_is_pressed('1'):
        ser.write("1")
        f.write("1 ")
    try:
        if keyboard.is_pressed('q'):
            ser.write("0")
            f.write("SESSION ENDED")
            break
        else:
            pass
    except:
        ser.write("0")
        f.write("Quit UNEXPECTED")
        print("\t!!!!\nIncorrect input, quit unexpected\n\t!!!!!!\n")
        break  # if user pressed a key other than the given key the loop will break


