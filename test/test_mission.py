from src.mission import Mission
from src.robot import Robot


def test_initialise_grid_successfully():
    # Arrange
    grid = Mission.initialise_grid("4 2")
    print(grid)
    assert len(grid) == 4
    assert len(grid[0]) == 2