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
        return f"{self.stop_name} on line {self.on_line}"

class LineData(BaseModel):
    line_name: str
    stops: List[Stop]

class Lines(BaseModel):
    lines: List[LineData]
