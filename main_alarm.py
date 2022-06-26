""" 

Project Name: Alarm Clock and backup of 10 minutes automatically
Author: Valentina Costin

"""
################
# Libraries
################

import os
import random
import webbrowser

#################
# Modules
#################
from alarm import ring_alarm

# Check if a txt file for youtube alarm not exist then create one
if not os.path.isfile("alarm_youtube.txt"):
    with open("alarm_youtube.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=VEMFlGJtoEU")

def alarm_user_input_checker(alarm_time):
    ''' 
    Check if the user has entered a valid alarm input 
    The possible format:  [Hour:Minute] or [Hour:Minute:Second] 
    '''

    if len(alarm_time) == 2: 
        #  [Hour:Minute]
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and  alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:
        #  [Hour:Minute:Second] 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and  alarm_time[1] < 60 and alarm_time[1] >= 0 and \
            alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True

    return False

if __name__ == '__main__':

    while True:
        # Get user input for the alarm time
        alarm_user_input = input("Set the alarm (Eg: 08:00): ")

        try:
            alarm_time = [int(n) for n in alarm_user_input.split(":")]

            if alarm_user_input_checker(alarm_time):
                # We intend to set a backup alarm at 10 minutes later than the user's initial alarm
                alarm_time_backup = [alarm_time[0], alarm_time[1] + 10]

                if alarm_time_backup[1] > 60: # change hour
                    alarm_time_backup[0] = alarm_time_backup[0] + 1
                    alarm_time_backup[1] = alarm_time_backup[1] - 60

                print("Backup: ", alarm_time_backup)

                #Call ring_alarm function for user and backup 
                ring_alarm(alarm_time)
                ring_alarm(alarm_time_backup)
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Please, enter time in HH:MM format")

 

