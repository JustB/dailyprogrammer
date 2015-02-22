# -*- coding: utf-8 -*-
#
# http://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/
#
# we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program
# that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too
# high or too low. Try to make a program that can guess your number based on user input and great code!

import random

low_end = 0
high_end = 100
correct = False
while not correct:
    guess = random.randint(low_end, high_end)
    print 'Your number is %d' % guess
    choice = raw_input('Is it too (h)igh or too (l)ow or (c)orrect? ')
    if choice == 'h':
        high_end = guess
    elif choice == 'l':
        low_end = guess
    elif choice == 'c':
        correct = True
    else:
        print 'Choose again!'

print 'I won!'
