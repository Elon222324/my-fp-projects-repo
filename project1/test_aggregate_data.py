import unittest
from src.aggregate_data import aggregate_data

class TestAggregateData(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(aggregate_data([1, 2, 3], "sum"), 6)

    def test_product(self):
        self.assertEqual(aggregate_data([1, 2, 3], "product"), 6)

    def test_min(self):
        self.assertEqual(aggregate_data([1, 2, 3], "min"), 1)

    def test_max(self):
        self.assertEqual(aggregate_data([1, 2, 3], "max"), 3)

    def test_invalid_operation(self):
        with self.assertRaises(TypeError):
            aggregate_data([1, 2, 3], "average")

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            aggregate_data([], "sum")
            
    def test_non_numeric_data(self):
        with self.assertRaises(TypeError):
            aggregate_data([1, 2, "three"], "sum")
        with self.assertRaises(TypeError):
            aggregate_data([1, 2, None], "sum")
        with self.assertRaises(TypeError):
            aggregate_data([1, 2, [3]], "sum")
            
    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            aggregate_data("not a list", "sum")
        with self.assertRaises(TypeError):
            aggregate_data(123, "sum")

if __name__ == '__main__':
    unittest.main()