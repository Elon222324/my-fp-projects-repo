import unittest
import time
from src.count_elements import count_elements

class TestCountElements(unittest.TestCase):
    def test_list(self):
        lst = [1, 2, 3, 4, 5, 6]
        func = lambda x: x%2==0
        self.assertEqual(count_elements(lst, func), 3)
        
    def test_tuple(self):
        tpl = (1, 2, 3, 4, 5, 6)
        func = lambda x: x%2==0
        self.assertEqual(count_elements(tpl, func), 3)    
        
    def test_set(self):
        st = {1, 2, 3, 4, 5, 6}
        func = lambda x: x%2==0
        self.assertEqual(count_elements(st, func), 3) 
        
    def test_empty_list(self):
        lst = []
        func = lambda x: x%2==0
        self.assertEqual(count_elements(lst, func), 0)    

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            lst = 123456
            func = lambda x: x%2==0
            count_elements(lst, func)
            
    def test_invalid_function(self):
        with self.assertRaises(TypeError):
            lst = [1, 2, 3, 4, 5, 6]
            func = 55654
            count_elements(lst, func)
                        
    def test_large_list_performance(self):
        large_lst = list(range(10000))
        func = lambda x: x%2==0
        start_time = time.time()
        count_elements(large_lst, func)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 1, f"Функция выполняется слишком долго: {execution_time} секунд")                  
  

if __name__ == '__main__':
    unittest.main()