from pydantic import BaseModel
from typing import List

class Stop(BaseModel):
    stop_name: str
    on_line: str
    def __hash__(self):
        return hash(self.stop_name)
    
    def __eq__(self, other):
        return other == self.stop_name

    def __str__(self):
        return f"Travel to {self.stop_name} on {self.on_line} line"

class LineData(BaseModel):
    line_name: str
    stops: List[Stop]

class Lines(BaseModel):
    lines: List[LineData]
