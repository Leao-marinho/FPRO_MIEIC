"""
Travelling

Write a Python program to help the user arrive in Lisbon at time.
Ask the user in how many hours and how many minutes 
she can spend travelling at most. 
Return the average velocity (in km/h) 
that she will need to drive to arrive in time. 
Assume the distance between Porto and Lisbon is 313 km.

Please round the result.

@author: Luísa Maria
"""

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

hour_from_minutes = minutes/60

average_velocity = 313 / (hours + hour_from_minutes)

result = round(average_velocity)

print(result)