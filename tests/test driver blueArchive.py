import unittest
from gachaSimulators import blueArchiveGacha as ba



class blue_archive_tests(unittest.TestCase):
    def test_something(self):
        sr = ba.summon_sim(50, False)
        self.assertIs(sr, list, "A list was not returned! Expected list")  # add assertion here


if __name__ == '__main__':
    unittest.main()
