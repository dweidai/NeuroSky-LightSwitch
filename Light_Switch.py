from NeuroPy import NeuroPy
import keyboard
import serial # if you have not already done so

def attention_callback(attention_value):
    #"this function will be called everytime NeuroPy has a new value for attention"
    print ("Value of attention is",attention_value)
    return None

if __name__ == '__main__':
    print("program started")
    #f = open("testfile.txt", "w")
    headset=NeuroPy("COM6") #If port not given 57600 is automatically assumed
    #headset=NeuroPy("/dev/cu.MindWaveMobile-SerialPort") #for linux
    ser = serial.Serial('/dev/tty.usbserial', 9600)

    #set call back:
    headset.setCallBack("attention",attention_callback)

    #call start method
    headset.start()
    confirm_meditate = 0
    confirm_attention = 0
    nb = input('To quit, press spacebar')
    #while True:
    #    if(object1.meditation>70): #another way of accessing data provided by headset (1st being call backs)
    #        object1.stop() #if meditation level reaches above 70, stop fetching data from the headset
    while True:
        if(headset.meditation > 70):
            confirm_meditation += 1
            confirm_attention = 0
        if(headset.attention > 70):
            confirm_attentation += 1
            confirm_meditation = 0
        if(confirm_meditaiton > 10):
            ser.write("0\n")
            f.write("0 ")
        elif(confirm_attention > 10):
            ser.write("1\n")
            f.write("1 ")
        try:
            if keyboard.is_pressed('q'):
                headset.stop()
                ser.write("0\n")
                ser.write("Session ended")
                f.write("SESSION ENDED")
                break
            else:
                pass
        except:
            headset.stop()
            ser.write("0\n")
            f.write("Quit UNEXPECTED")
            print("\t!!!!\nIncorrect input, quit unexpected\n\t!!!!!!\n")
            break  # if user pressed a key other than the given key the loop will break


