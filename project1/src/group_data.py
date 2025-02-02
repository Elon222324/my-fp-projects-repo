from typing import Any, Callable, Dict, List, Set
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def group_data(data:List[Any], key:Callable) -> Dict[Any, List[Any]]:
    """
    Функция принимает список и группирует по ключу. Возвращает словарь.
    data: Список элементов для группировки.
    key: функция, которая возвращает ключ для каждого элемента.
    
    The function takes a list and groups by key. Returns a dictionary.
    data: List of items to group.
    key: Function that returns the key for each item.
    """
    try:
        if not callable(key):
            raise TypeError("Переданный аргумент 'key' должен быть функцией.")
        if not isinstance(data, list):
            raise TypeError("Переданный аргумент 'data' не является списком")               
        new_dct = dict()
        for item in data:
            x = key(item)
            if x not in new_dct:
                new_dct[x] = [item]
            else:
                new_dct[x].append(item)
        return new_dct
    except Exception as e:
        logger.error(f"Ошибка: {e}. data: {data}, key: {key}")
        raise               
