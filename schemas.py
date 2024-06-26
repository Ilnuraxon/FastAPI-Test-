
from typing import Optional
from pydantic import BaseModel, ConfigDict

class STaskId(BaseModel):
    ok: bool = True
    task_id: int


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int
    

    model_config = ConfigDict(from_attributes=True)


