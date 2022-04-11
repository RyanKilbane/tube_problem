from pydantic import BaseModel
from typing import List

class Stop(BaseModel):
    stop_name: str
    on_line: str
    def __hash__(self):
        return hash(self.stop_name)

class LineData(BaseModel):
    line_name: str
    stops: List[Stop]

class Lines(BaseModel):
    lines: List[LineData]
