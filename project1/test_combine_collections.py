import unittest
from src.combine_collections import combine_collections

class TestСombineСollections(unittest.TestCase):
    def test_shorter_list_and_tuple(self):
        lst = [1, 2, 3, 4]
        tpl = ("A", "B", "C")
        self.assertEqual(combine_collections(lst, tpl), [(1, "A"),(2, "B"),(3, "C")])
        
    def test_list_and_tuple(self):
        lst = [7, 8, 9]
        tpl = ("A", "B", "C")
        self.assertEqual(combine_collections(lst, tpl), [(7, "A"),(8, "B"),(9, "C")])
        
    def test_list_and_list(self):
        lst = [7, 8, 9]
        lst2 = ["A", "B", "C"]
        self.assertEqual(combine_collections(lst, lst2), [(7, "A"),(8, "B"),(9, "C")])        
        
    def test_empty_list_and_empty_tuple(self):
        lst = []
        tpl = ()
        self.assertEqual(combine_collections(lst, tpl), [])
 
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            lst = [7, 8, 9]
            smt = "hfhfhf"
            combine_collections(lst, smt)               
        
        
        
if __name__ == '__main__':
    unittest.main()