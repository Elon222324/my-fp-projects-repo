from typing import Callable, Any, List, Tuple, Union
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def filter_data(data: Union[List[Any], Tuple[Any, ...]], 
                func: Callable[[Any], bool]) -> Union[List[Any], Tuple[Any, ...]]:
    """
    Фильтрует элементы переданной коллекции(списки и кортежи) с помощью переданной функции.
    В случае ошибки, возвращает пустое значение такого же типа, что и входящие данные.
    data: коллекция для преобразования(list, tuple)
    func: функция, которая применятся к каждому элементу коллекции.
    
    Filters the elements of the given collection (lists and tuples) using the given function.
    In case of an error, returns an empty value of the same type as the input data.
    data: the collection to transform (list, set)
    func: the function to apply to each element of the collection.
    """
    tp = type(data)
    if not callable(func):
            raise TypeError("Переданный аргумент 'func' должен быть функцией.")
    try:
        if isinstance(data, (list, tuple)):
            return tp(filter(func, data))
    except  Exception as e:
        logger.error(f"Ошибка: {e}")
        return tp()
    raise TypeError("Поддерживаются только списки и кортежи.")