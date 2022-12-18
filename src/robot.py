from enum import Enum

class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        
    def __repr__(self):
        return f"Robot is in coordinates ({self.x}, {self.y}), facing direction {self.direction}"

    def move_forward(self):
        direction = Direction[self.direction]
        print(direction, "fish")
        if direction == Direction.N:
            self.y += 1
        elif direction == Direction.E:
            self.x += 1
        elif direction == Direction.S:
            self.y += -1
        elif direction == Direction.W:
            self.x += -1

    def rotate_left(self):
        self.direction = Direction((Direction[self.direction].value - 2) % 4 + 1).name

    def rotate_right(self):
        self.direction = Direction((Direction[self.direction].value ) % 4 + 1).name