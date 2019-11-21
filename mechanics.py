"""
Mechanics

A king needs your help to defend his castle! 
He will tell you the angle of his cannon (in degrees) 
and you will tell him how far (horizontally) 
the cannon ball will go (until it hits the ground).

The cannon ball fires at the velocity of 18 m/s. 
Air resistance (drag) is negligible. 
Assume g=-10m/s². Please round the result.

Some code is already provided for you:

import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

@author: Luísa Maria
"""

import math

angle = int(input("Angle: "))* math.pi/180  # converts to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

time = (18 * sin_angle) / 5

final_position = ((18 * cos_angle) * time)

result = round(final_position)

print(result)
