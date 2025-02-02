from typing import Any, Sequence, Union, Dict, List, Tuple, Set
import logging
from functools import reduce

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def aggregate_data(data: Sequence[Union[int, float]], operation:str) -> Union[int, float]:
    """
    Функция для выполнения операции агрегации на списке данных.
    data: Список чисел (int или float).
    operation: Операция для выполнения ('sum', 'min', 'max', 'product').
    
    Function to perform an aggregation operation on a list of data.
    data: List of numbers (int or float).
    operation: Operation to perform ('sum', 'min', 'max', 'product').
    """
    if operation not in ("sum", "min", "max", "product"):
        raise TypeError("Переданный аргумент 'operation' не является операцией.")
    if not isinstance(data, (list, tuple)):
        raise TypeError("Переданный аргумент 'data' не является списком")  
    if not data:
        raise ValueError("Список данных не может быть пустым.") 
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Все элементы 'data' должны быть числами (int или float).") 
    try:            
        if operation == "sum":
            return sum(data)
        elif operation == "min":
            return min(data)
        elif operation == "max":
            return max(data)
        elif operation == "product":
            return reduce(lambda x, y: x * y, data)
    except Exception as e:
        logger.error(f"Ошибка: {e}. data: {data}, key: {operation}")
        raise         
