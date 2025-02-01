import unittest
from src.nested_collections import nested_collections

class TestNestedCollections(unittest.TestCase):
    def test_nested_list(self):
        items = [1, [2, 3], [4, [5, 6]]]
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), [2, [3, 4], [5, [6, 7]]])

    def test_nested_tuple(self):
        items = (1, (2, 3), (4, (5, 6)))
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), (2, (3, 4), (5, (6, 7))))

    def test_nested_set(self):
        items = {1, (2, 3), (4, (5, 6))}
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), {2, (3, 4), (5, (6, 7))})
        
    def test_nested_dict(self):
        items = {"a": 1, "b": [2, 3], "c": {"d": 4, "e": [5, 6]}}
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), {"a": 2, "b": [3, 4], "c": {"d": 5, "e": [6, 7]}})    
        
    def test_nested_empty_list(self):
        items = []
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), [])    
          
    def test_with_different_items(self):
        items = [1, (2, 3), [4, {5, 6}]]
        func = lambda x: x + 1
        self.assertEqual(nested_collections(items, func), [2, (3, 4), [5, {6, 7}]])  
        
    def test_sort_invalid_type(self):
        items = "not a list"
        func = lambda x: x + 1
        with self.assertRaisesRegex(TypeError, "Переданный аргумент не является коллекцией"): nested_collections(items, func) 
            
    def test_sort_key_is_not_callable(self):
        items = [1, (2, 3), [4, {5, 6}]]
        func = "not_a_function"
        with self.assertRaisesRegex(TypeError, "Переданный аргумент 'func' должен быть функцией."): nested_collections(items, func)
                                    
                      
if __name__ == '__main__':
    unittest.main()