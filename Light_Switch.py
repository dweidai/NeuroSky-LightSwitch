from NeuroPy.NeuroPy import NeuroPy
import serial
import keyboard
import time


print("program started")
f = open("testfile.txt", "w") #just a txt file to keep track of the record
ser = serial.Serial('/dev/tty.usbmodem14201', 9600) #connect to the arduino
print("aruidno connected")
headset = NeuroPy("/dev/cu.MindWaveMobile-SerialPo", 57600) #connect to the Neurosky Headset
print("heatset initialized")
time.sleep(0.1)

# writing to arduino serial to turn on light
def light_on():
    ser.write('1')

# writing to arduino serial to turn off light
def light_off():
    ser.write('0')

# asking Neuropy to return the attention value
def attention_callback(attention_value):
    return attention_value

# asking Neuropy to return the meditation value
def meditation_callback(meditation_value):
    return meditation_value

#start reading data
headset.start()
print("headset started")

confirm_meditate = 0 #counting number of iterations to confirm data sending
confirm_attention = 0
attention_threshold = 85 #set by hand
meditation_threshold = 75 #set by hand, should be different for each subject
iteration = 7 # 7 is a lucky number and 0.7 seconds is a reasonable focus time

while True:
    #extract values from the headset
    attention = headset.setCallBack("attention",attention_callback)
    meditation = headset.setCallBack("meditation", meditation_callback)
    time.sleep(0.1)
    '''print("Attention: ", attention) #print to the terminal
    print("Meditation: ", meditation)'''
    f.write(str(attention)+ "\t" (str(meditation)+ "\n") #write to the file
    if(meditation > meditation_threshold):
        confirm_meditation += 1
        confirm_attention = 0
    if(attention > attention_threshold):
        confirm_attentation += 1
        confirm_meditation = 0
    if(confirm_meditaiton > iteration): #only send the value if it pass certain number of iterations
        light_on()
    elif(confirm_attention > iteration):
        light_off()

    try: #if the user press control+c or q, the program will stop and shut down neurosky
        if keyboard.is_pressed('q'):
            headset.stop()
            print("headset closed")
            break
        else:
            pass
    except:
        headset.stop()
        print("headset closed")
        break
