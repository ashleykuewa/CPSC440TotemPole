import subprocess
import os

fuelpath = 'C:\\Users\\Origi\\Documents\\GitHub\\CPSC440TotemPole\\dist\\Fuel.txt'


def main():
    filepath = 'C:\\Users\\Origi\\Documents\\GitHub\\CPSC440TotemPole\\dist\\outer.exe'

    try:
        while True:  # input("Enter any key to continue...") != KeyboardInterrupt:
            os.startfile(filepath)
            #subprocess.call(filepath)
            # Start the party
            # Wait for file to end
            key = input("Enter any key to continue...\n")  # wait for user input
            if key == 'j':
                forward()
                os.startfile(filepath)
            elif key == 'f':
                back()
                os.startfile(filepath)
            elif key == 'q':
                print("Program terminated")
                break
            else:
                print("Only f and j are inputs")
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
