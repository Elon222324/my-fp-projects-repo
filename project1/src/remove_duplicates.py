from typing import List
import logging
from collections.abc import Hashable

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def remove_duplicates(data: List[Hashable]) -> List[Hashable]:
    """
    Удаляет дубликаты из списка. Порядок сохраняется. Возвращает итог ввиде списка.
    data: список, содержащий только хешируемые объекты.
    
    Removes duplicates from a list. Order is preserved. Returns the result as a list.
    data: a list containing only hashable objects.
    """
    if not isinstance(data, list):
        raise TypeError("Переданный аргумент 'data' не является списком")
    if not all(isinstance(x, Hashable) for x in data):
        raise TypeError("Список data должен содержать только хешируемые объекты.")
    try:   
        st_data = set()
        new_lst = []
    
        for item in data:
            if item not in st_data:
                st_data.add(item)
                new_lst.append(item)
        return new_lst
    except Exception as e:
        logger.error(f"Ошибка: {e}. data: {data}")
        raise  