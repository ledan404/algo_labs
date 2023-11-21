"""
This module contains functions for performing a topological sort 
on a directed acyclic graph and writing the optimal order of tasks to an output file.

Functions:
- topological_sort(graph: dict) -> list: Perform a topological sort on a directed acyclic graph.
- optimal_order(input_file: str, output_file: str) -> None: Reads a file containing dependencies 
  between tasks and writes to an output file the optimal order in which to perform the tasks.
"""


def topological_sort(graph) -> list:
    """
    Perform a topological sort on a directed acyclic graph.

    Args:
        graph (dict): A dictionary representing the graph.
        The keys are nodes and the values are lists of neighbors.

    Returns:
        list: A list of nodes in topologically sorted order.
    """
    visited = set()
    result = []

    def dfs(node) -> None:
        """
        Depth-fist search algorithm that traverses a graph starting from a given node.

        Args:
            node: The starting node for the traversal.

        Returns:
            None
        """
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    return result


def optimal_order(input_file, output_file):
    """
    Reads a file containing dependencies between tasks and writes
    to an output file the optimal order in which to perform the tasks.

    Args:
    - input_file (str): path to the input file containing dependencies between tasks
    - output_file (str): path to the output file to write
    the optimal order in which to perform the tasks

    Returns:
    - None
    """
    dependencies = {}
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            tokens = line.strip().split()
            current, prerequisite = tokens[0], tokens[1]
            dependencies.setdefault(current, []).append(prerequisite)
    order = topological_sort(dependencies)

    with open(output_file, "w", encoding="utf-8") as file:
        for item in order:
            file.write(item + "\n")


if __name__ == "__main__":
    optimal_order("govern.in", "govern.out")
