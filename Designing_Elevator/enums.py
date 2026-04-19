from enum import Enum

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"
           
class RequestType(Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"