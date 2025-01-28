from typing import Iterable, Callable, Any
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def count_elements(collect: Iterable[Any], func: Callable[[Any], bool]) -> int:
    """
    Функция возвращает количество элементов коллекции, удовлетворяющих переданному условию.
    Если возникает ошибка, выбрасывается исключение.
    collect: коллекция
    func: функция-условие
    
    The function returns the number of elements in the collection that satisfy the passed condition.
    If an error occurs, an exception is raised.
    collect: collection
    func: condition function
    """
    try:
        if not callable(func):
            raise TypeError("Переданный аргумент 'func' должен быть функцией.")
        if not isinstance(collect, Iterable):
            raise TypeError("Переданный аргумент не является коллекцией")
        else:
            return len(list(filter(func, collect)))
        
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise        
    
#a = 565
#func = 5656
#print(count_elements(a, func))
    
    