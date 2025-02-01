from typing import Callable, Any, List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def sort_items(collect: List[Any], key: Callable[[Any], Any], reverse: bool = False) -> List[Any]:
    """
    Функция сортировки, которая принимает список элементов и ключ сортировки (функцию key), 
    и возвращает отсортированный список в зависимости от значения, возвращаемого функцией key. 
    Сортировка выполняется по возрастанию (по умолчанию). 
    Если возникает ошибка, выбрасывается исключение.
    collect: список (list)
    key: функция, которая применяется к каждому элементу списка для извлечения ключа сортировки.
    reverse: флаг для сортировки в обратном порядке (по умолчанию False).
    
    A sorting function that takes a list of elements and a sort key (the key function),
    and returns a sorted list based on the value returned by the key function.
    The sorting is in ascending order (the default).
    If an error occurs, an exception is raised.
    collect: list (list)
    key: a function that is applied to each element of the list to extract the sorting key.
    reverse: a flag for sorting in reverse order (default is False).
    """
    try:
        if not callable(key):
            raise TypeError("Переданный аргумент 'key' должен быть функцией.")
        if not isinstance(collect, list):
            raise TypeError("Переданный аргумент 'collect' не является списком")
        else:
            try:
                return sorted(collect, key=key, reverse=reverse)
            except KeyError as e:
                raise ValueError(f"Ошибка при извлечении значения для сортировки: {e}")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise