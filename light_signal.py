
# signal simulator
# the function return a random generated state of the signal.
# it returns a pair of values ['green'|'red', <time_left>]


from numpy import random

def signal_state():
    s = random.randint(0, 2)
    colour = 'red'
    if s == 1:
        colour = 'green'

    time_left = random.randint(1, 81)

    return [colour, time_left]
