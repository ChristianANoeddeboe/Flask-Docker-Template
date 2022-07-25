
from datetime import datetime

from pydantic import BaseModel

class BaseAuditableEntity(BaseModel):

    created: datetime
    created_by: str = None
    modified: datetime = None
    modified_by: str = None