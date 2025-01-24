from typing import Any, List, Tuple, Union
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def enumerate_items(collect: Union[List[Any], Tuple[Any, ...]]) -> List[Tuple[int, Any]]:
    """
    Функция возвращает список кортежей (индекс, значение) для каждого элемента в коллекции.
    collect: коллекции типа List, Tuple
    The function returns a list of tuples (index, value) for each element in the collection.
    collect: collections of type List, Tuple
    """
    if not isinstance(collect, (tuple, list)):
        raise TypeError("Переданный аргумент не является списком или кортежем")
    new_lst = []
    try:
        for num, item in enumerate(collect):
            new_lst.append((num, item))
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        
            
    return new_lst

print(enumerate_items(("a", "b", "c")))