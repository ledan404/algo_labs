"""Zenyk and maricka"""


def robot_gardener(m, n, garden):
    result = []
    for row in range(m):
        if row % 2 == 0:
            result.extend(garden[row])
        else:
            result.extend(garden[row][::-1])
    return result
