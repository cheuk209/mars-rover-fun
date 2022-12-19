import pytest
from src.robot import *
from src.mission import *

def test_robot_has_correct_locations():
    # Arrange
    robot = Robot(0, 0, "E", initialise_grid("10 10"))
    
    # Act
    expected = "Robot is in coordinates (0, 0), facing direction E"
    
    # Assert
    assert repr(robot) == expected

def test_robot_will_not_launch_if_location_invalid():
    # Act
    with pytest.raises(Exception) as e_info:
        robot = Robot(12, 12, "E", initialise_grid("10 10"))
    # Assert
    assert str(e_info.value) == "(12, 12) is an invalid location to launch robot."


left_rotation = [("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N")]
@pytest.mark.parametrize("initial_direction, post_direction", left_rotation)
def test_robot_has_correct_orientation_after_left_rotation(initial_direction, post_direction):
    # Arrange
    robot = Robot(0, 0, initial_direction, initialise_grid("10 10"))
    
    # Act
    robot.rotate_left()
    
    # Assert
    assert post_direction == robot.direction

right_rotation = [("N", "E"),
                ("W", "N"),
                ("S", "W"),
                ("E", "S")]
@pytest.mark.parametrize("initial_direction, post_direction", right_rotation)
def test_robot_has_correct_orientation_after_right_rotation(initial_direction, post_direction):
    # Arrange
    robot = Robot(0, 0, initial_direction, initialise_grid("10 10"))
    
    # Act
    robot.rotate_right()
    
    # Assert
    assert post_direction == robot.direction

move_forward_commands = [((1, 1, "E"), (2, 1, "E")),
                         ((1, 1, "N"), (1, 2, "N")),
                         ((2, 3, "S"), (2, 2, "S")),
                         ]
@pytest.mark.parametrize("initial_position, post_position", move_forward_commands)
def test_robot_can_move_forward_to_correct_locations(initial_position, post_position):
    # Arrange
    robot = Robot(*initial_position, initialise_grid("10 10"))
    
    # Act
    robot.move_forward()
    
    # Assert
    assert robot.direction == initial_position[2]
    assert (robot.x, robot.y, robot.direction) == post_position