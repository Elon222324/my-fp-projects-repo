import unittest
from src.filter_data import filter_data

class TestFilterData(unittest.TestCase):
    def test_filter_numbers(self):
        data = [1, 2, 3, 4, 5]
        condition = lambda x: x > 3
        self.assertEqual(filter_data(data, condition), [4, 5])

    def test_filter_strings(self):
        data = ["apple", "banana", "cherry", "date"]
        condition = lambda x: "a" in x
        self.assertEqual(filter_data(data, condition), ["apple", "banana", "date"])

    def test_filter_by_length(self):
        data = ["hi", "hello", "hey", "world"]
        condition = lambda x: len(x) > 3
        self.assertEqual(filter_data(data, condition), ["hello", "world"])

    def test_empty_data(self):
        self.assertEqual(filter_data([], lambda x: True), [])
        self.assertEqual(filter_data((), lambda x: True), ())
        
    def test_tuple_input(self):
        data = (1, 2, 3, 4, 5)
        condition = lambda x: x % 2 == 0
        self.assertEqual(filter_data(data, condition), (2, 4))
        
    def test_unsupported_data_type(self):
        with self.assertRaises(TypeError):
            filter_data({1, 2, 3}, lambda x: x > 1)
            
    def test_invalid_condition(self):
        with self.assertRaises(TypeError):
            filter_data([1, 2, 3], "not a function")
        


if __name__ == '__main__':
    unittest.main()
