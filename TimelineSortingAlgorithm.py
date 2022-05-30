from asyncore import loop
import DateOfEvent

loop_flag = False
date_class = DateOfEvent.Date_of_Event

while loop_flag != True:
    name_event = input("Name of event:\n")
    date_class.__init__(date_class, input("Date of event:\n"))
    stop = input("Stop?: y/n\n")
    if stop == 'y':
        loop_flag = True