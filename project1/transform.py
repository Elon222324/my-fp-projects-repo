from typing import Iterable, Callable, Any
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def transform_collection(data: Iterable[Any], func: Callable[[Any], Any]) -> Iterable[Any]:
    """
    Преобразует элементы коллекции с помощью переданной функции.
    В случае ошибки функция возврает пустой список и логирует проблему.
    data: коллекция для преобразования(list, tuple, set)
    func: функция, которая применятся к каждому элементу коллекции.
    
    Transforms the elements of a collection using the passed function. Supported types: list, tuple, set.
    In case of an error, the function always returns an empty list.
    data: collection to transform(list, tuple, set)
    func: function to apply to each element of the collection
    """
    try:
        if isinstance(data, list):
            return list(map(func, data))                    
        elif isinstance(data, tuple):
            return tuple(map(func, data))
        elif  isinstance(data, set):
            return set(map(func, data))
        else:
            raise TypeError(f"Тип данных {type(data).__name__} не поддерживается")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []

#list
print(transform_collection([1, 2, "3"], lambda x: x ** 2))
print(transform_collection(["apple", "orange"], len))
print(transform_collection(["apple", "orange"], lambda x: x.upper()))
print(transform_collection([(1, 2), (3, 4)], str))

#tuple
print(transform_collection((1, 2, 3, 4, "5") , lambda x: x ** 2))

#set
print(transform_collection({1, 2, 3, 4, 5} , lambda x: x ** 2))
print(transform_collection({"dog", "cat", "mouse"} , lambda x: x[::-1]))

print(transform_collection(123 , lambda x: x**2))