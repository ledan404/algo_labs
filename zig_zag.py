"""Zenyk and maricka"""


def robot_gardener(m: int, n: int, garden: list) -> list: # pylint: disable=unused-argument
    """
    Returns the path of the robot gardener.

    Args:
        m: The number of rows in the garden.
        n: The number of columns in the garden.
        garden: List of lists representing the garden.
    Returns:
        The path of the robot gardener.
    """
    result = []
    for row in range(m):
        if row % 2 == 0:
            result.extend(garden[row])
        else:
            result.extend(garden[row][::-1])
    return result
