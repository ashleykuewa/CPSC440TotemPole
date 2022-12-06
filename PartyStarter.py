#import TextDisplay.py
from subprocess import call
import RPi.GPIO as GPIO
import time

fuelpath = '/home/ashleyjosh/Documents/440Proj/CPSC440TotemPole-main/Fuel.txt'


def main():
    GPIO.setmode (GPIO.BOARD)
    GPIO.setwarnings(False)
    
    button1 = 8
    button2 = 10
    
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    filepath = '/home/ashleyjosh/Documents/440Proj/CPSC440TotemPole-main/TextDisplay.py'
    
    try:
        while True:
            print("Waiting for input")
            if GPIO.input(button1) == GPIO.HIGH:
                forward()
                call(["python", "TextDisplay.py"])
                #break
            if GPIO.input(button2) == GPIO.HIGH:
                back()
                call(["python", "TextDisplay.py"])
                #break
            
            #os.startfile(filepath)
            #print("Party starting")
            
            #call(["python", "TextDisplay.py"])
            # subprocess.Popen(['sh', filepath])
            # Start the party
            # Wait for file to end
 
            # key = input("Enter any key to continue...\n")  # wait for user input
            
            
            #print("Party ended")
            #time.sleep(5.0)
                
            #if key == 'j':
                #forward()
                #call(["python", "TextDisplay.py"])
            #elif key == 'f':
                #back()
                #call(["python", "TextDisplay.py"])
            #elif key == 'q':
                #print("Program terminated")
                #break
            #else:
                #print("Only f and j are inputs")
    except KeyboardInterrupt:
        print("Terminated")


def forward():  # Forward button is pressed and the program increments the message array
    print("Forward we go")
    with open(fuelpath) as f:
        lines = f.readlines()
        index = int(lines[0])
        print(index)
        if index < len(lines) - 1:
            lines[0] = str(index + 1) + '\n'
        else:
            print("Index cannot go higher")
    with open(fuelpath, "w") as file:
        file.writelines(lines)


def back():  # Back button is pressed and the program decrements the message array
    print("Backward we go")
    with open(fuelpath, "r") as f:
        lines = f.readlines()
        index = int(lines[0])
        print(index)
        if index != 0:
            lines[0] = str(index - 1) + '\n'
        else:
            print("Index cannot go lower")
        with open(fuelpath, "w") as file:
            file.writelines(lines)


main()
