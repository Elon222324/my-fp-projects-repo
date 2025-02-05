import unittest
from src.remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_no_duplicates(self):
        data = [1, 2, 3, 4]
        result = remove_duplicates(data)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_with_duplicates(self):
        data = [1, 2, 2, 3, 4, 4]
        result = remove_duplicates(data)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_empty_list(self):
        data = []
        result = remove_duplicates(data)
        self.assertEqual(result, [])

    def test_single_element(self):
        data = [1]
        result = remove_duplicates(data)
        self.assertEqual(result, [1])

    def test_mixed_types(self):
        data = [1, "string", 1.5, "string", 1]
        result = remove_duplicates(data)
        self.assertEqual(result, [1, "string", 1.5])

    def test_non_hashable_elements(self):
        data = [[1, 2], [2, 3], [1, 2]]
        with self.assertRaises(TypeError):
            remove_duplicates(data)

    def test_mixed_hashable_and_non_hashable(self):
        data = [1, [1, 2], "hello"]
        with self.assertRaises(TypeError):
            remove_duplicates(data)

if __name__ == "__main__":
    unittest.main()