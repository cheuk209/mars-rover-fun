from src.mission import *
from src.robot import *
import pytest

def test_initialise_grid_successfully():
    # Arrange
    test_grid = initialise_grid("4 2")
    
    # Assert
    assert len(test_grid) == 4
    assert len(test_grid[0]) == 2
    
def test_initlise_empty_grid_is_unsuccessful():
    # Arrange
    test_grid = "-1 -1"
    
    # Act
    with pytest.raises(Exception) as e_info:
        result = initialise_grid(test_grid)
        
    # Assert
    assert str(e_info.value) == "Grid dimension must be greater than 0"

consecutive_commands = [((1, 1, "N"), (1, 4, "N"), "FFF"),
                        ((1, 1, "N"), (1, 1, "E"), "LLL"),
                        ((1, 1, "N"), (1, 1, "W"), "RRR")]
@pytest.mark.parametrize("initial_position, post_position, robot_command", consecutive_commands)
def test_move_robot_consecutive_commands_are_successful(initial_position, post_position, robot_command):
    # Arrange
    test_robot = Robot(*initial_position, initialise_grid("10 10"))
    
    # Act
    move_robot(test_robot, robot_command, initialise_grid("4 4"))
    new_position = Robot(*post_position, initialise_grid("10 10"))
    
    # Assert
    assert repr(test_robot) == repr(new_position)
    
def test_get_final_locations_of_robot_successfully():
    # Arrange
    test_grid = initialise_grid("8 8")
    test_mission_commands = ["(2, 3, N) FFLFR"]
    
    # Act
    result = get_final_positions(test_mission_commands, test_grid)
    
    # Assert
    assert result == ["(1, 5, N)"]
    
def test_get_final_locations_when_commands_are_empty():
    # Arrange
    test_grid = initialise_grid("8 8")
    test_mission_commands = ["(2, 3, N) "]
    
    # Act
    result = get_final_positions(test_mission_commands, test_grid)
    
    # Assert
    assert result == ["(2, 3, N)"]
    
def test_get_final_locations_of_multiple_robots_successfully():
    # Arrange
    test_grid = initialise_grid("8 8")
    test_mission_commands = ["(2, 3, N) FLLFR", "(1, 1, E) FF", "(0, 0, W) RF"]
    
    # Act
    result = get_final_positions(test_mission_commands, test_grid)
    
    # Assert
    assert result == ["(2, 3, W)", "(3, 1, E)", "(0, 1, N)"]

lost_locations = [
    (["(0, 3, S) FFFFF"], ["(0, 0, S) LOST"]),
    (["(3, 2, E) FFF"], ["(4, 2, E) LOST"]),
    (["(3, 1, S) FLRRFFFFFF"], ['(0, 0, W) LOST'])
    ]
@pytest.mark.parametrize("mission_commands, expected_locations", lost_locations)
def test_get_final_identified_location_of_lost_robot(mission_commands, expected_locations):
    # Arrange
    test_grid = initialise_grid("4 4")
    
    # Act
    result = get_final_positions(mission_commands, test_grid)
    
    # Assert
    assert result == expected_locations
    
def test_launch_mission_is_successful():
    # Arrange
    test_input = """4 8\n(2, 3, E) LFRFF\n(0, 2, N) FFLFRFF"""
    print(test_input)
    # Act
    results = launch_mission(test_input)
    
    # Assert
    assert results == "The results are:\n(4, 4, E)\n(0, 4, W) LOST"
    