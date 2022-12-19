import re
from robot import Robot
import warnings

def launch_mission(input):
    instructions = input.strip().split("\n")
    
    grid_dimension = instructions[0]   
    grid = initialise_grid(grid_dimension)
    print(grid)
    
    mission_commands = instructions[1:]
    final_positions = get_final_positions(mission_commands, grid)
    return "The results are:\n" + "\n".join(final_positions)

def initialise_grid(grid_dimension):
    # split the input string into lines
    lines = grid_dimension.strip().split("\n")

    # parse the grid size from the first line
    m, n = map(int, lines[0].split())

    # initialize the grid with a default value
    grid = [[None for _ in range(n)] for _ in range(m)]
    
    if len(grid) == 0 or len(grid[0]) == 0:
        raise ValueError(f"Grid dimension must be greater than 0")
    return grid

def move_robot(robot, actions, grid):
    for action in actions:
        if not (0 <= robot.x < len(grid) and 0 <= robot.y < len(grid[0])):
            if not 0 <= robot.x < len(grid):
                x_bounds = [0, len(grid)]
                robot.x = min(x_bounds, key=lambda x:abs(x-robot.x))
                return f"({robot.x}, {robot.y}, {robot.direction}) LOST"
            elif not 0 <= robot.y < len(grid[0]):
                y_bounds = [0, len(grid[0])]
                robot.y = min(y_bounds, key=lambda y:abs(y-robot.y))
                return f"({robot.x}, {robot.y}, {robot.direction}) LOST"
        if action == "F":
            robot.move_forward()
        elif action == "L":
            robot.rotate_left()
        elif action == "R":
            robot.rotate_right()
        else:
            raise ValueError(f"Robot cannot comprehend your command :( {action}")
    return f"({robot.x}, {robot.y}, {robot.direction})"

def get_final_positions(mission_commands, grid):
    final_positions = []

    for command in mission_commands:
        # split the line into the initial position and actions
        initial_pos, actions = command.rsplit(" ", 1)

        # parse the initial position
        x, y, orientation = initial_pos[1:-1].split(", ")
        x, y = int(x), int(y)
        orientation = orientation.upper()

        # create a robot with the initial position and direction
        robot = Robot(x, y, orientation, grid)

        # move the robot according to the actions
        robot_destination = move_robot(robot, actions, grid)

        final_positions.append(robot_destination)
    return final_positions


    

# example input
input_str = """
4 8
(2, 3, N) FLLFR
(1, 0, S) FFRLF
"""

input_str_2 = """
4 8
(0, 4, E) LFRFF
(0, 2, N) FFLFRFF
"""

# execute the commands for the robots
final_countdown = launch_mission(input_str_2)
print(final_countdown)

# alternatively prompt for user input
# def main():
#   user_input = ""
#   while True:
#       line = input("Please enter robot coordinates and commands:")
#       if line:
#           user_input += line + "\n"
#       else:
#           break

#   print(f'You entered: {user_input}')
#   results = launch_mission(user_input)
#   print(results)

# if __name__ == '__main__':
#   main()