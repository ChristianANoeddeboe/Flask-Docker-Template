
from backend.domain.common.BaseAuditableEntity import BaseAuditableEntity


class TodoListItem(BaseAuditableEntity):

    id: int
    list_id: int
    title: str
    note: str
    is_done: bool
