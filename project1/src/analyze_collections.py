from typing import Callable, Any, List, Tuple, Union
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def all_check(collection: Union[List, Tuple], func: Callable[[Any], bool]) -> bool:
    """
    Принимает коллекцию и проверяет, выполняются ли все элементы коллекции согласно заданному условию
    collection:коллекция для преобразования(list, tuple)
    func:функция, которая применятся к каждому элементу коллекции    
    
    Takes a collection and checks whether all elements of the collection satisfy a given condition
    collection:collection to transform(list, tuple)
    func:function to apply to each element of the collection
    """
    if not callable(func):
            raise TypeError("Переданный аргумент 'func' должен быть функцией.")
    try:
        if isinstance(collection, (list, tuple)):
            return all((map(func, collection)))
    except  Exception as e:
        logger.error(f"Ошибка: {e}")
        return False
    raise TypeError("Поддерживаются только списки и кортежи.")        

def any_check(collection: Union[List, Tuple], func: Callable[[Any], bool]) -> bool:
    """
    Принимает коллекцию и проверяет, выполняется ли хотя бы одно условие среди всех элементов коллекции.
    collection:коллекция для преобразования(list, tuple)
    func:функция, которая применятся к каждому элементу коллекции
    
    Takes a collection and checks if at least one condition is met among all elements of the collection.
    collection:collection to transform(list, tuple)
    func:function to apply to each element of the collection
    """
    if not callable(func):
            raise TypeError("Переданный аргумент 'func' должен быть функцией.")
    try:
        if isinstance(collection, (list, tuple)):
            return any(map(func, collection))
    except  Exception as e:
        logger.error(f"Ошибка: {e}")
        return False 
    raise TypeError("Поддерживаются только списки и кортежи.")

print(any_check((), lambda x: "Python" in x))