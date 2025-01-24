import unittest
from unittest.mock import patch
from project1.src.transform import transform_collection

class TestTransformCollection(unittest.TestCase):
    
    def test_list_transform(self):
        data = [1, 2, 3, 4]
        result = transform_collection(data, lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_tuple_transform(self):
        data = (1, 2, 3, 4)
        result = transform_collection(data, lambda x: x * 2)
        self.assertEqual(result, (2, 4, 6, 8))

    def test_set_transform(self):
        data = {1, 2, 3, 4}
        result = transform_collection(data, lambda x: x * 2)
        self.assertEqual(result, {2, 4, 6, 8})

    def test_invalid_data_type(self):
        data = "not a collection"
        result = transform_collection(data, lambda x: x * 2)
        self.assertEqual(result, [])

    def test_empty_data(self):
        data = []
        result = transform_collection(data, lambda x: x * 2)
        self.assertEqual(result, [])
        
    def test_wrong_item(self):
        data = [1, 2, 3, "4"]
        result = transform_collection(data, lambda x: x ** 2)
        self.assertEqual(result, [])
        
    @patch('transform.logger')  # Проверка логирования
    def test_logging_on_error(self, mock_logger):
        data = [1, 2, 3, "4"]
        transform_collection(data, lambda x: x ** 2)
        mock_logger.error.assert_called_with("Ошибка: unsupported operand type(s) for ** or pow(): 'str' and 'int'")


if __name__ == '__main__':
    unittest.main()

