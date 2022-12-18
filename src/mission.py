import re
from robot import Robot

class Mission:
    def __init__(self, input):
        self.instructions = input.strip().split("\n")
    
    def mission_commence(self):
        grid_dimension = self.instructions[0]
        grid = self.initialise_grid(grid_dimension)
        
        robot_commands = self.instructions[1:]
        result = self.get_final_positions(robot_commands, grid)
        return result
    
    def initialise_grid(self, grid_dimension):
        # split the input string into lines
        lines = grid_dimension.strip().split("\n")

        # parse the grid size from the first line
        m, n = map(int, lines[0].split())

        # initialize the grid with a default value
        grid = [[None for _ in range(n)] for _ in range(m)]
        
        if len(grid) == 0 or len(grid[0]) == 0:
            raise ValueError(f"Grid dimension must be non-zero")
        return grid
        # iterate over the remaining lines
        
    def get_final_positions(self, mission_commands, grid):
        final_positions = []

        for command in mission_commands:
            # split the line into the initial position and actions
            initial_pos, actions = command.rsplit(" ", 1)
            # parse the initial position
            x, y, orientation = initial_pos[1:-1].split(", ")
            x, y = int(x), int(y)
            orientation = orientation.upper()

            # create a robot with the initial position and direction
            robot = Robot(x, y, orientation)

            # move the robot according to the actions
            self.move_robot(robot, actions)

            # check if the robot is lost
            if not (0 <= robot.x < len(grid) and 0 <= robot.y < len(grid[0])):
            # mark the grid cell as lost
                grid[x][y] = "LOST"
                final_positions.append(f"{robot.x} {robot.y} {robot.direction} LOST")
            else:
                final_positions.append(f"{robot.x} {robot.y} {robot.direction}")

        return final_positions

    def move_robot(self, robot, actions):
        for action in actions:
            if action == "F":
                robot.move_forward()
            elif action == "L":
                robot.rotate_left()
            elif action == "R":
                robot.rotate_right()
            else:
                raise ValueError(f"Robot cannot comprehend your command :( {action}")
    

# example input
# input_str = """
# 4 8
# (2, 3, N) FLLFR
# """

input_str = """
0 1
(2, 3, N) FLLFR
"""
# execute the commands for the robots
final_countdown = Mission(input_str)
final_countdown.mission_commence()

# print the final positions
# print(final_positions)