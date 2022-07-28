
from backend.domain.common.BaseAuditableEntity import BaseAuditableEntity


class TodoListItem(BaseAuditableEntity):

    id: int
    list_id: int
    title: str
    note: str
    _done: bool

    def is_done(self):
        return self._done
    
    def set_done(self, value):
        self._done = value
