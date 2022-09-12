
from typing import Callable, Generic, TypeVar

_T = TypeVar("_T")

class DbSet(set, Generic[_T]):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find(self, func: Callable[[_T], bool]) -> _T | None:
        for item in self:
            if func(item):
                return item
        return None

    def find_all(self, func: Callable[[_T], bool]) -> list[_T]:
        return [item for item in self if func(item)]

    async def find_async(self, func: Callable[[_T], bool]) -> _T | None:
        return self.find(func)

    async def find_all_async(self, func: Callable[[_T], bool]) -> list[_T]:
        return self.find_all(func)

    async def to_list_async(self) -> list[_T]:
        return list(self)

    def to_list(self) -> list[_T]:
        return list(self)