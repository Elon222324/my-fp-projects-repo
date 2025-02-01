from typing import Any, Callable, Union, Dict, List, Tuple, Set
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def nested_collections(collect: Union[List[Any], Tuple[Any, ...], Set[Any], Dict[Any, Any]], 
    func: Callable[[Any], Any]
    ) -> Union[List[Any], Tuple[Any, ...], Set[Any], Dict[Any, Any]]:
    """
    Рекурсивно обрабатывает вложенную коллекцию, применяя функцию func к каждому элементу.
    collect: коллекция (list, tiple, set, dict).
    func: функция, которая применяется к каждому элементу коллекции.
     
    Recursively processes a nested collection, applying a function func to each element.
    collect: a collection of (list, tiple, set, dict).
    func: a function that is applied to each element of the collection.
    """
    
    try:
        if not callable(func):
            raise TypeError("Переданный аргумент 'func' должен быть функцией.")
        if not isinstance(collect, (list, tuple, set, dict)):
            raise TypeError("Переданный аргумент не является коллекцией")    
        
        if isinstance(collect, (list, tuple, set)):
            type_collect = type(collect)
            return type_collect(func(x) if not isinstance(x, (list, tuple, set, dict)) else nested_collections(x, func) for x in collect)
        elif isinstance(collect, dict):
            return {
                nested_collections(a, func) if isinstance(a, (list, tuple, set, dict)) else a: 
                nested_collections(b, func) if isinstance(b, (list, tuple, set, dict)) else func(b)
                for a, b in collect.items()
            }
        
        return func(collect)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise     