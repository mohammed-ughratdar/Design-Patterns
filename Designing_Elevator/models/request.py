from enums import Direction, RequestType

class Request:
    def __init__(self, target_floor: int, direction: Direction, request_type: RequestType):
        self.target_floor = target_floor
        self.direction = direction
        self.request_type = request_type

    def get_target_floor(self):
        return self.target_floor

    def get_direction(self):
        return self.direction

    def get_request_type(self):
        return self.request_type