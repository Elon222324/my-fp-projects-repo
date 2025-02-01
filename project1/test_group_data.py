import unittest
from src.group_data import group_data

class TestGroupData(unittest.TestCase):
    def test_group_data(self):
        data = [1, 2, 3, 4, 5, 6]
        result = group_data(data, key=lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4, 6]}

    def test_group_data_empty(self):
        result = group_data([], key=lambda x: x)
        assert result == {}        
        
    def test_group_data_invalid_input(self):
        data = "not a list"
        with self.assertRaisesRegex(TypeError, "Переданный аргумент 'data' не является списком"): group_data(data, key=lambda x: x) 
    
    def test_group_data_key_error(self):
        data = [1, 2, 3, 4, 5, 6]
        with self.assertRaisesRegex(TypeError, "Переданный аргумент 'key' должен быть функцией."): group_data(data, key="not_a_function") 
               
    def test_group_data_str(self):
        data = ["apple", "banana", "cherry", "avocado"]
        result = group_data(data, key=lambda x: x[0])
        self.assertEqual(result, {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']})  
        

    def test_group_data_tuple_keys(self):
        data = [("apple", 1), ("banana", 2), ("cherry", 1), ("avocado", 2)]
        result = group_data(data, key=lambda x: x[1])
        self.assertEqual(result, {1: [('apple', 1), ('cherry', 1)], 2: [('banana', 2), ('avocado', 2)]})    
        
    def test_group_data_none_key(self):
        data = [1, 2, 3, 4, 5]
        result = group_data(data, key=lambda x: None)
        self.assertEqual(result, {None: [1, 2, 3, 4, 5]})
          
if __name__ == '__main__':
    unittest.main()