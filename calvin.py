

# I am worried and showing the logic and write a most readable code possible.
# I am mantioning that because it has some performance imporvements that could be done

import pdb
import matplotlib.pyplot as plt
import numpy

from light_signal import signal_state

NO_JORNEYS = 100000


def waiting_time(signal, wand_used, no_wand_allowed_uses, signals_remaining, time_left_to_use_wand):
    #pdb.set_trace()
    if signal[0] == 'red':
        if signals_remaining <= no_wand_allowed_uses - wand_used:
            wand_used += 1
            return  [0, wand_used]
        if signal[1] > time_left_to_use_wand and wand_used < no_wand_allowed_uses:
            wand_used += 1
            return  [0, wand_used]
        else:
            return [signal[1], wand_used]
    return [0, wand_used]

def best_choice():
    # asks for how many signal is on the way and how many times de wand can be used.
    no_signals = int(input('How many signals? '))
    no_wand_allowed_uses = int(input('How many wand times? '))
    jorneys_avg_time = {}
    for time_left_to_use_wand in range(1, 81):
        total_time = 0
        for i in range(1, NO_JORNEYS + 1):
            jorney_time = 0
            wand_used = 0
            no_remaining_signals = no_signals

            for s in range(1, no_signals + 1):
                signal = signal_state()
                r = waiting_time(signal, wand_used, no_wand_allowed_uses, no_remaining_signals, time_left_to_use_wand)
                jorney_time += r[0]
                wand_used = r[1]
                no_remaining_signals -= 1



            total_time += jorney_time

        avg_time = total_time/NO_JORNEYS
        jorneys_avg_time[time_left_to_use_wand] = avg_time


        x = []
        y = []
        #pdb.set_trace()
        for k,v in jorneys_avg_time.items():
            x.append(k)
            y.append(v)


    plt.plot(x, y, 'ro')
    plt.ylabel('Avarage')
    plt.xlabel('Time left when using the wand')
    plt.show()

def main(time_left_to_use_wand):
    # asks for how many signal is on the way and how many times de wand can be used.
    no_signals = int(input('How many signals? '))
    no_wand_allowed_uses = int(input('How many wand times? '))


    jorneys = {}
    jorneys_time = []

    #pdb.set_trace()
    total_time = 0

    for i in range(1, NO_JORNEYS + 1):
        jorney_time = 0
        wand_used = 0
        no_remaining_signals = no_signals

        for s in range(1, no_signals + 1):
            signal = signal_state()
            r = waiting_time(signal, wand_used, no_wand_allowed_uses, no_remaining_signals, time_left_to_use_wand)
            jorney_time += r[0]
            wand_used = r[1]
            no_remaining_signals -= 1

        jorneys_time.append(jorney_time)
        if jorney_time in jorneys:
            jorneys[jorney_time] += 1
        else:
            jorneys[jorney_time] = 1

        total_time += jorney_time

    avg_time = numpy.mean(jorneys_time)
    std = numpy.std(jorneys_time)
    x = []
    y = []
    #pdb.set_trace()
    zeros = 0
    for k,v in jorneys.items():
        x.append(k)
        y.append(v)
        if k == 0:
            zeros = v

    p_zeros = zeros/NO_JORNEYS
    print('avarage: ' + str(avg_time))
    print('std: ' + str(std))
    print('percent of zeros: ' + str(p_zeros))
    plt.axvline(x=avg_time)
    plt.axvline(x=std, c='r')
    plt.plot(x, y,'ro')
    plt.ylabel('Ocurrency')
    plt.xlabel('Jorney Time')
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    #best_choice()
    main(20)
