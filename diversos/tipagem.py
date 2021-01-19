"""
Estudo de tipagem em python
"""
'''
from typing import List, Tuple, Union


def concatena(ti: Union[List, Tuple, int],
              t2: Union[List, Tuple, int]
              ) -> Union[List, Tuple, int]
    return ti + t2
'''


from typing import Any


def concatena(ti: Any, t2: Any) -> Any:
    return ti + t2
