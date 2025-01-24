import unittest
import time
from src.enumerate_items import enumerate_items

class TestEnumerateItems(unittest.TestCase):
    def test_list(self):
        lst = ["a", "b", "c", "d"]
        self.assertEqual(enumerate_items(lst), [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')])
        
    def test_tuple(self):
        tpl = ("a", "b", "c", "d")
        self.assertEqual(enumerate_items(tpl), [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')])
        
    def test_empty_list(self):
        lst = []
        self.assertEqual(enumerate_items(lst), [])
        
    def test_empty_tuple(self):
        tpl = ()
        self.assertEqual(enumerate_items(tpl), [])
        
    def test_different_items(self):
        lst = [568, "a", [1, 2, 3], {1:"a"}]
        self.assertEqual(enumerate_items(lst), [(0, 568), (1, 'a'), (2, [1, 2, 3]), (3, {1: 'a'})])       
        
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            smt = 454546454
            enumerate_items(smt)
    
    def test_large_list_performance(self):
        large_lst = list(range(10000))
        start_time = time.time()
        enumerate_items(large_lst)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 1, f"Функция выполняется слишком долго: {execution_time} секунд")
        
        
if __name__ == '__main__':
    unittest.main()