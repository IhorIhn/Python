import unittest

def sum_from_string(s):
    if not isinstance(s, str):
        return "Не можу це зробити"
    try:
        parts = s.split(',')
        numbers = [int(p.strip()) for p in parts]
        return sum(numbers)
    except:
        return "Не можу це зробити"

class TestSumFromString(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(sum_from_string("1,2,3,4"), 10)
        self.assertEqual(sum_from_string("1,2,3,4,50"), 60)

    def test_invalid_input(self):
        self.assertEqual(sum_from_string("qwerty1,2,3"), "Не можу це зробити")
        self.assertEqual(sum_from_string("a,b,c"), "Не можу це зробити")

    def test_empty_string(self):
        self.assertEqual(sum_from_string(""), "Не можу це зробити")

    def test_single_number(self):
        self.assertEqual(sum_from_string("5"), 5)

    def test_spaces_between_numbers(self):
        self.assertEqual(sum_from_string("1, 2, 3"), 6)
        self.assertEqual(sum_from_string(" 1 , 2 , 3 "), 6)

    def test_invalid_letters_only(self):
        self.assertEqual(sum_from_string("hello,world"), "Не можу це зробити")

    def test_none_input(self):
        self.assertEqual(sum_from_string(None), "Не можу це зробити")

    def test_double_commas(self):
        self.assertEqual(sum_from_string("1,,2"), "Не можу це зробити")
        self.assertEqual(sum_from_string("1,,2,3"), "Не можу це зробити")

    def test_irrelevant_data(self):
        self.assertEqual(sum_from_string("10000000,99993999393939,7777"), 10000000 + 99993999393939 + 7777)

    def test_non_string_values(self):
        self.assertEqual(sum_from_string([1, 2, 3]), "Не можу це зробити")

if __name__ == '__main__':
    unittest.main(verbosity=2)
