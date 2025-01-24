import unittest
import time
from src.analyze_collections import all_check, any_check

class TestAnalyzeCollectionsAll(unittest.TestCase):
    # Тесты для функции all_check
    def test_list_all(self):
        lst = [1, 3, 5, 6]
        func = lambda x: x % 2 == 0
        self.assertEqual(all_check(lst, func), False)
        
    def test_tuple_all(self):
        tpl = ("I love Python", "Python is great", "Python")
        func = lambda x: "Python" in x
        self.assertEqual(all_check(tpl, func), True)
        
    def test_empty_list_all(self):
        lst = []
        func = lambda x: "Python" in x
        self.assertEqual(all_check(lst, func), True)
        
    def test_empty_tuple_all(self):
        tpl = ()
        func = lambda x: "Python" in x
        self.assertEqual(all_check(tpl, func), True)     
        
    def test_invalid_type_all(self):
        with self.assertRaises(TypeError):
            func = lambda x: x > 0
            smt = 454546454
            all_check(smt, func)
            
    def test_mixed_types_all(self):
        lst = [1, "Python", 3.5]
        func = lambda x: isinstance(x, str)
        self.assertEqual(all_check(lst, func), False)
    
    def test_large_list_performance_all(self):
        large_lst = list(range(10000))
        func = lambda x: 9999 == x
        start_time = time.time()
        all_check(large_lst, func)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 1, f"Функция выполняется слишком долго: {execution_time} секунд")
        
class TestAnalyzeCollectionsAny(unittest.TestCase):
    # Тесты для функции any_check
    def test_list_any(self):
        lst = [1, 3, 5, 6]
        func = lambda x: x % 2 == 0
        self.assertEqual(any_check(lst, func), True)
        
    def test_tuple_any(self):
        tpl = ("I love Python", "Python is great", "Python")
        func = lambda x: "Python" in x
        self.assertEqual(any_check(tpl, func), True)
        
    def test_empty_list_any(self):
        lst = []
        func = lambda x: "Python" in x
        self.assertEqual(any_check(lst, func), False)
        
    def test_empty_tuple_any(self):
        tpl = ()
        func = lambda x: "Python" in x
        self.assertEqual(any_check(tpl, func), False)     
        
    def test_invalid_type_any(self):
        with self.assertRaises(TypeError):
            smt = 454546454
            func = lambda x: x > 0
            any_check(smt, func)
            
    def test_mixed_types_any(self):
        lst = [1, "Python", 3.5]
        func = lambda x: isinstance(x, str)
        self.assertEqual(any_check(lst, func), True)
    
    def test_large_list_performance_any(self):
        large_lst = list(range(10000))
        func = lambda x: 9999 == x
        start_time = time.time()
        any_check(large_lst, func)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 1, f"Функция выполняется слишком долго: {execution_time} секунд")
        
    def test_large_list_performance_any_early_exit(self):
        large_lst = [9999] + list(range(1000000))
        func = lambda x: x == 9999
        start_time = time.time()
        result = any_check(large_lst, func)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertTrue(result)
        self.assertLess(execution_time, 1, f"Функция выполняется слишком долго: {execution_time} секунд")
        
        
if __name__ == '__main__':
    unittest.main()