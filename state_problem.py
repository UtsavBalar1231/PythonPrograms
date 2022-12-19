import json
from tracemalloc import start

# Load state space of Romania problem
input_statespace = open('input_statespace.txt', 'r').read()

# Split the input into lines
input_statespace = input_statespace.splitlines()

# Remove first element of the list
input_statespace.remove(input_statespace[0])

# Split the data into a list of lists
input_statespace = [x.split(':') for x in input_statespace]

# Extract the start state and goal state
start_state = input_statespace.pop(0)[0]
goal_state = input_statespace.pop(0)[0]

# Processing of the input data as per the problem
# state: next_state_1,cost next_state_2,cost
input_statespace = [[x[0], x[1].split()] for x in input_statespace]
input_statespace = [[x[0], [y.split(',') for y in x[1]]]
                    for x in input_statespace]

# Convert the cost from string to integer
input_statespace = [
    [x[0], [[y[0], int(y[1])] for y in x[1]]] for x in input_statespace]

# Convert the entire statespace list to a dictionary
input_statespace = dict(input_statespace)

# Print the state space dictionary
# print(json.dumps(input_statespace, indent=4))

print('Start state: {}'.format(start_state))
print('End state: {}'.format(goal_state))
print('State space size: {}'.format(len(input_statespace)))
print('Total Transitions: {}'.format(
    sum([len(x) for x in input_statespace.values()])))

# Load input heuristic values
input_heuristic = open('input_heuristic.txt', 'r').read()

# Split the input into lines
input_heuristic = input_heuristic.splitlines()

# Split the data into a list of lists
input_heuristic = [x.split(': ') for x in input_heuristic]

# Convert the heuristic values from string to integer
input_heuristic = [[x[0], int(x[1])] for x in input_heuristic]

# Convert the entire heuristic list to a dictionary
input_heuristic = dict(input_heuristic)

# Print the heuristic dictionary
# print(json.dumps(input_heuristic, indent=4))


# A* search algorithm implementation
class Node:
    """
    The Node class is used to represent a node in the search tree.
    """

    def __init__(self, state, parent, actions, cost, heuristic):
        """
        The constructor of the Node class. It initializes the state, parent, actions, cost and heuristic values.
        """
        self.state = state
        self.parent = parent
        self.g = cost
        self.h = heuristic
        self.f = self.g + self.h
        self.actions = actions

    def __lt__(self, other):
        """
        The __lt__ method is used to compare two nodes based on their f values.
        """
        return self.f < other.f

    def __eq__(self, other):
        """
        The __eq__ method is used to compare two nodes based on their state values.
        """
        return self.state == other.state

    def __hash__(self):
        """
        The __hash__ method is used to return the hash value of the node.
        This allows us to use the node as a key in a dictionary.
        """
        return hash(self.state)

    def __repr__(self):
        """
        The __repr__ method is used to return the string representation of the node.
        Example: ('Arad', 366)
        """
        return ('({0}, {1})'.format(self.state, self.f))


class AStar:
    """
    The AStar class is used to represent the A* search algorithm.
    """

    def __init__(self, start_state, goal_state, statespace, heuristic):
        """
        The constructor of the AStar class. It initializes the start_state, goal_state, statespace and heuristic values.
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.statespace = statespace
        self.heuristic = heuristic
        self.total_cost = 0

    def search(self):
        """
        The search method is used to search for the goal state using the A* search algorithm.
        """
        # Create the start node
        start_node = Node(self.start_state, None, None, 0,
                          self.heuristic[self.start_state])

        # Create the frontier and explored sets
        frontier = set()
        explored = set()

        # Add the start node to the frontier set
        frontier.add(start_node)

        # Loop until the frontier set is empty
        while frontier:
            # Get the node with the lowest f value
            current_node = min(frontier)

            # Check if the current node is the goal state
            if current_node.state == self.goal_state:
                self.total_cost += current_node.g
                path = self.get_path(current_node)

                # Print the explored states
                self.print_visited_states(explored)

                print('Found path of length {} with total cost {}'.format(
                    len(path), self.total_cost))

                # print the path in the required format
                self.print_path(path)

                # Return True to indicate that the goal state was found
                return True

            # Remove the current node from the frontier set
            frontier.remove(current_node)

            # Add the current node to the explored set
            explored.add(current_node)

            # Get the next states
            next_states = self.statespace[current_node.state]

            # Loop through the next states
            for next_state in next_states:
                # Create the next node
                next_node = Node(next_state[0], current_node, next_state[1],
                                 current_node.g + next_state[1], self.heuristic[next_state[0]])

                # Check if the next node is in the explored set
                if next_node in explored:
                    continue

                # Check if the next node is in the frontier set
                if next_node in frontier:
                    # Get the node from the frontier set
                    frontier_node = [x for x in frontier if x == next_node][0]

                    # Check if the next node has a lower f value
                    if next_node.f < frontier_node.f:
                        # Remove the frontier node from the frontier set
                        frontier.remove(frontier_node)

                        # Add the next node to the frontier set
                        frontier.add(next_node)
                else:
                    # Add the next node to the frontier set
                    frontier.add(next_node)

        # Return None if no path is found
        return None

    def get_path(self, node):
        """
        The get_path method is used to get the path from the start state to the goal state.
        """
        # Create the path
        path = []

        # Loop until the node is None
        while node:
            # Add the node to the path
            path.append(node)

            # Get the parent node
            node = node.parent

        # Reverse the path
        path = path[::-1]

        # Return the path
        return path

    def print_visited_states(self, explored):
        """
        The print_visited_states method is used to print the visited states.
        """
        # Loop through the path
        print('States visited:', end=' ')
        print(', '.join([x.state for x in explored]))

    def print_path(self, path):
        """
        The print_path method is used to print the path from the start state to the goal state.
        """
        # Loop through the path
        for node in path:
            if node.state != self.goal_state:
                print(node.state, end=' => ')
        print(self.goal_state)
        print()


if __name__ == '__main__':
    # Create an instance of the A* search algorithm
    astar = AStar(start_state, goal_state, input_statespace,
                  input_heuristic)

    if not astar.search():
        print('Goal state not found!')
