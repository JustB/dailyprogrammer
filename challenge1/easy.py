# -*- coding: utf-8 -*-
#
# http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
# create a program that will ask the users name, age, and reddit username. have it tell them the information back,
# in the format:
# your name is (blank), you are (blank) years old, and your username is (blank)
# for extra credit, have the program log this information in a file to be accessed later.



name = raw_input("What's your name? ")
age = raw_input('How old are you? ')
username = raw_input("What's your reddit username? ")

output = 'Your name is %s, you are %d years old and your reddit username is %s' % (name, int(age), username)
print output

out_file = open('reddit.txt', 'w')
out_file.write(output)
out_file.close()