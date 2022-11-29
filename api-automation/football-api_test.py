import unittest
from football_api import get_football_competitions

class MyTestCase(unittest.TestCase):
    def test_competitions_count(self):
        competition_count = get_football_competitions()
        self.assertGreater(competition_count, 100)  # add assertion here


if __name__ == '__main__':
    unittest.main()
