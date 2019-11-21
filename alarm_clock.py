"""
Alarm clock

Write a script that given an hour and minutes by user input, 
prints at what time the alarm clock will ring, 
knowing that the current hour is hour and the current minutes are minutes. 
The clock goes off after 6 hour and 51 minutes.

@author: Luísa Maria
"""

hour = int(input("Hour: "))
minutes = int(input("Minutes: "))
        
ring_hour = hour + 6
    
while(ring_hour >= 24):
    ring_hour = ring_hour - 24
    ring_hour = ring_hour % 24        
    
ring_minutes = minutes + 51
    
while(ring_minutes >= 60):
    ring_minutes = ring_minutes - 60
    ring_hour = ring_hour + 1
        
ring_minutes = ring_minutes % 60
    
    
print(str("{:02d}".format(ring_hour)) + ":" + str("{:02d}".format(ring_minutes)))


