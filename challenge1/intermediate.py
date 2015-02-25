# -*- coding: utf-8 -*-
# Create a menu driven program
# Using the menu drive program allow a user to add/delete items
# The menu should be based on an events calendar where users enter the events by hour
# No events should be hard-coded.


events = {}

print '*' * 80
print 'Events calendar'
print '*' * 80

def prompt():
    print 'Would you like to (a)dd, (e)dit, (d)elete, (l)ist; or (q)uit?'
    choice = raw_input('?> ')
    return choice

choice = prompt()
while choice != 'q':
    if choice == 'a':
        print 'Add an element'
        hour = raw_input('Hour?> ')
        description = raw_input('Description?> ')
        if hour not in events:
            events[hour] = description
    elif choice == 'd':
        print 'Delete an element'
        hour = raw_input('Hour?> ')
        if hour in events:
            del events[hour]
    elif choice == 'e':
        print 'Edit an element'
        hour = raw_input('Hour?> ')
        description = raw_input('Description?> ')
        if hour in events:
            events[hour] = description
    elif choice == 'l':
        print 'List elements'
        for key in sorted(events):
            print '%s => %s' % (key, events[key])
    else:
        pass
    choice = prompt()

print 'Goodbye'