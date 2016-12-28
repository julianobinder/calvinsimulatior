import unittest


from calvin import waiting_time
from light_signal import signal_state

class TestCalvinDecision(unittest.TestCase):
    time_left_to_use_wand = 40


    def test_green_over_time(self):
        # should not use the wand and waiting time should be 0

        signal = ['green',50]
        wand_used = 0
        r = waiting_time(signal, wand_used, 1, 10, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,0)
        self.assertEqual(t,0)

    def test_green_under_time(self):
        # should not use the wand and waiting time should be 0

        signal = ['green',40]
        wand_used = 0
        r = waiting_time(signal, wand_used, 1, 10, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,0)
        self.assertEqual(t,0)

    def test_red_use_saved_wand(self):
        # Calvin will devide to use the wand when he can use it more time than the remaining signals on the way.
        # should use the wand and waiting time should be 0

        signal = ['red',40]
        wand_used = 0
        r = waiting_time(signal, wand_used, 1, 1, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,1)
        self.assertEqual(t,0)

    def test_red_not_use_wand(self):
        # should not use the wand and waiting time should be 40

        signal = ['red',40]
        wand_used = 0
        r = waiting_time(signal, wand_used, 1, 10, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,0)
        self.assertEqual(t,40)

    def test_red_use_wand_exceed(self):
        # should NOT use the wand and waiting time should be 50

        signal = ['red',50]
        wand_used = 1
        r = waiting_time(signal, wand_used, 1, 10, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,1)
        self.assertEqual(t,50)

    def test_red_use_wand(self):
        # should use the wand and waiting time should be 0

        signal = ['red',50]
        wand_used = 0
        r = waiting_time(signal, wand_used, 1, 10, self.time_left_to_use_wand)
        t = r[0]
        wand_used = r[1]
        self.assertEqual(wand_used,1)
        self.assertEqual(t,0)

class TestSignalState(unittest.TestCase):

    def test_green_red(self):

        NO_OF_ROLLS = 10000
        sum_of_n = 0
        for i in range(0, NO_OF_ROLLS):
            signal = signal_state()
            if signal[0] == 'green':
                sum_of_n += 1
            else:
                sum_of_n += 2

        self.assertEqual(round(sum_of_n/NO_OF_ROLLS,1),1.5)

    def test_time_left(self):

        NO_OF_ROLLS = 100000
        sum_of_n = 0
        for i in range(0, NO_OF_ROLLS):
            signal = signal_state()
            sum_of_n += signal[1]

        self.assertEqual(int(sum_of_n/NO_OF_ROLLS),40)
