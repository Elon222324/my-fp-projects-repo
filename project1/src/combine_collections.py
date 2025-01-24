from typing import Any, List, Tuple, Union
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def combine_collections(*args: Union[List[Any], Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:
    """
    Функция принимает произвольное количество коллекций (списков или кортежей) 
    и объединяет их поэлементно в список кортежей.
    args: коллекции типа list, tuple
    The function takes an arbitrary number of collections (lists or tuples) and combines them element-wise into a list of tuples.
    args: collections of type list, tuple
    """
    for i in args:
            if not isinstance(i, (tuple, list)):
                raise TypeError("Переданный аргумент не является списком или кортежем")
    try: 
        return list(zip(*args))
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []
    
    