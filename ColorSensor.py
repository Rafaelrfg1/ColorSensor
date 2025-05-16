from machine import Pin, I2C
from color_sensor import ColorSensor
import time

# Initialize I2C and sensor
i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=100000)
sensor = ColorSensor(i2c)

# Get and print a single color reading
color, (r, g, b, c) = sensor.get_color()
print(f"Detected color: {color}")
print(f"Raw values - R: {r}, G: {g}, B: {b}, C: {c}")
# Initialize sensor as before
#I will use this function to establish whether or not the robot is near the line connecting the black matte and the white tape
#def isNearTheLine(color):
  #  if color == "White":
   #     return True
    #else:
     #   return None
    #Might not even need this function but just incase
#Here i initaizlize the counter as zero for all the disks as at the start we have not yet reached any
redCounter = 0
greenCounter = 0
blueCounter = 0
#This function detects the color and returns the string of that color's name, which we will then use to give instructions to the rest of the team's parts to respond to
def colorIs(color, redCounter, greenCounter, blueCounter):
    if color == "Red":
        redCounter = 1
        return "Red"
    elif color == "Green":
        greenCounter = 1
        return "Green"
    elif color == "Blue":
        blueCounter = 1
        return "Blue"
    elif color == "Black":
        return "Black"
    elif color == "White":
        return "White"
#This is mainly for the motor team, which will give the motor team the "clearance to give power to the wheels continuously or to adjust if we are on the line
def instructionSensor (color):
    if color == "White":
        return 'Turn Right 2 clicks and Go Forward for 4 ticks' #We will make a future if statement that if this statement is returned, then the motors will respond accordingly
    elif color == "Black":
        return 'Go Forward Continuously'  #Also a for a future if statement for the motor team
    else:
        return 'Stop' #The idea here is if it is not reading black or white, then it must be a color which will make it stop. 

#This is just a test while loop for my own research. We will start merging our codes soon
while True:
    # Get both color and normalized values
    color, (r, g, b, c) = sensor.get_color()
    r_ratio, g_ratio, b_ratio, _ = sensor.get_normalized_values()
    
    # Print results
    print("Color is " + str(colorIs(color,redCounter, greenCounter, blueCounter)))
    print(f"Raw - R: {r}, G: {g}, B: {b}, C: {c}")
    #print(f"Normalized - R: {r_ratio:.1f}, G: {g_ratio:.1f}, B: {b_ratio:.1f}")
    #print("-" * 50)
    print("\nIs on the line?   " + str(isNearTheLine(color)))
    print("\nWhat do I do? " + str(instructionSensor(color)))
    time.sleep(1)
