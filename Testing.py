import unittest

from matchingSocks import matchingSocks


class Testing(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_case1(self):
        unMatched = [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]
        matched = matchingSocks(unMatched)
        self.assertEqual(4, len(matched))

    def test_case2(self):
        unMatched = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        matched = matchingSocks(unMatched)
        self.assertEqual(3, len(matched))

    def test_case3(self):
        unMatched = [1, 3, 5, 7, 8, 1, 4, 4, 5, 9, 8, 3, 5, 6, 10, 11, 4, 2, 1, 9]
        matched = matchingSocks(unMatched)
        self.assertEqual(6, len(matched))

    def test_case4(self):
        unMatched = [3, 5, 7, 9, 3, 6, 5, 4, 1, 0, 1, 6, 9, 7, 9, 8, 3, 9, 0, 3]
        matched = matchingSocks(unMatched)
        self.assertEqual(9, len(matched))


if __name__ == '__main__':
    unittest.main()

