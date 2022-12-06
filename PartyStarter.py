import subprocess

filepath = '../GitHub/CPSC440TotemPole/Party.py'
try:
    while True: # input("Enter any key to continue...") != KeyboardInterrupt:
        # subprocess.call(filepath)  # Start the party
        # Wait for file to end
        input("Enter any key to continue...")  # wait for user input
except KeyboardInterrupt:
    print("Terminated")


def forward(): # Forward button is pressed and the program increments the message array
    with open("../GitHub/CPSC440TotemPole/Fuel.txt") as f:
        lines = f.readlines()
        index = int(lines[0])
        if index > len(lines):
            lines[0] = index + 1
    with open("../GitHub/CPSC440TotemPole/Fuel.txt", "w") as f:
        f.writelines(lines)


def back(): # Back button is pressed and the program decrements the message array
    with open("../GitHub/CPSC440TotemPole/Fuel.txt") as f:
        lines = f.readlines()
        index = int(lines[0])
        if index != 0:
            lines[0] = index - 1
    with open("../GitHub/CPSC440TotemPole/Fuel.txt", "w") as f:
        f.writelines(lines)