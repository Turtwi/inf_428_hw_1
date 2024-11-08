import unittest

def calc_cyclic_time_difference(hour1: int, hour2: int) -> int:
    time_diff = 0
    while hour1 != hour2:
        hour1 += 1
        time_diff += 1
        if(hour1 == 24):
            hour1 = 0
    return time_diff

def calc_cyclic_time_difference_2(hour1: int, hour2: int) -> int:
    return (hour2 - hour1 + 24) % 24

class TestCalcCyclicTimeDifference(unittest.TestCase):
    def test_cyclic_time(self):
        self.assertEqual(calc_cyclic_time_difference(5, 6), 1)
        self.assertEqual(calc_cyclic_time_difference_2(3, 10), 7)
        self.assertEqual(calc_cyclic_time_difference(22, 2), 4)
        self.assertEqual(calc_cyclic_time_difference_2(5, 5), 0)
        self.assertEqual(calc_cyclic_time_difference(23, 0), 1)

if __name__ == "__main__":
    unittest.main()