import unittest
from src.sort_items import sort_items

class TestSortItems(unittest.TestCase):

    def test_sort_by_attribute(self):
        items = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        sorted_items = sort_items(items, key=lambda x: x['age'])
        self.assertEqual(sorted_items, [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}])

    def test_sort_reverse(self):
        items = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        sorted_items = sort_items(items, key=lambda x: x['age'], reverse=True)
        self.assertEqual(sorted_items, [{'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}])

    def test_empty_list(self):
        items = []
        sorted_items = sort_items(items, key=lambda x: x['age'])
        self.assertEqual(sorted_items, [])

    def test_invalid_key(self):
        items = [{'name': 'Alice', 'age': 30}]
        with self.assertRaises(ValueError):
            sort_items(items, key=lambda x: x['non_existing_key'])
            
    def test_sort_with_different_key(self):
        items = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        sorted_items = sort_items(items, key=lambda x: len(x['name']))
        assert sorted_items == [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

    def test_sort_invalid_type(self):
        items = "not a list"
        try:
            sort_items(items, key=lambda x: x['age'])
        except TypeError as e:
            assert str(e) == "Переданный аргумент 'collect' не является списком"

    def test_sort_key_is_not_callable(self):
        items = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        try:
            sort_items(items, key='not_a_function')
        except TypeError as e:
            assert str(e) == "Переданный аргумент 'key' должен быть функцией."

    def test_sort_with_missing_key(self):
        items = [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}]
        try:
            sort_items(items, key=lambda x: x['age'])
        except ValueError as e:
            assert str(e) == "Ошибка при извлечении значения для сортировки: 'age'"

if __name__ == '__main__':
    unittest.main()