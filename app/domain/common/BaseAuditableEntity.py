
from datetime import datetime

class BaseAuditableEntity:

    created: datetime
    created_by: str = None
    modified: datetime = None
    modified_by: str = None