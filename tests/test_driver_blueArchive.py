import unittest
from gachaSimulators.blueArchiveGacha import summon_sim


class blue_archive_tests(unittest.TestCase):
    def test_summon_sim(self):
        sr = summon_sim(200, False)
        self.assertIsInstance(sr, list, "A list was not returned! Expected list")


if __name__ == '__main__':
    unittest.main()
