data = open('input_statespace.txt', 'r').read().splitlines()

# Remove first element of the list
data.remove(data[0])

# Split the data into a list of lists
data = [i.split(':') for i in data]

# Extract the start state and goal state
start_state = data.pop(0)
goal_state = data.pop(0)

# Processing of data
# Split data into list of lists according to the state: next_state_1,cost next_state_2,cost
# [[state, [next_state_1,cost], [next_state_2,cost]], ...]
data = [[i[0], i[1].split()] for i in data]
data = [[i[0], [j.split(',') for j in i[1]]] for i in data]
# print(data)

# Convert the cost from string to integer
data = [
    [x[0], [[y[0], int(y[1])] for y in x[1]]] for x in data]

# Convert to dictionary for easy access
# {state: [[next_state_1, cost], [next_state_2, cost]], ...}
data = dict(data)

# print(data)

print("Start state: ", start_state)
print("Goal state (s): ", goal_state)
print("State space size: ", len(data))
print("Total transitions: ", sum([len(i) for i in data.values()]))

# Load input heuristic values
heuristic_data = open('input_heuristic.txt', 'r').read().splitlines()

# Split the data into a list of lists
heuristic_data = [i.split(': ') for i in heuristic_data]

# Convert the heuristic values from string to integer
heuristic_data = [[x[0], int(x[1])] for x in heuristic_data]

# Convert the entire heuristic list to a dictionary
heuristic_data = dict(heuristic_data)

# print(heuristic_data)


class Node:
    """ Node class to store the state, parent, cost and heuristic """

    def __init__(self, state, parent, cost, heuristic):
        """ Initialize the node with the state, parent, cost and heuristic """
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __repr__(self):
        """ Print the node in the required format """
        return f"Node({self.state}, {self.parent}, {self.cost}, {self.heuristic})"

    def __eq__(self, other):
        """ Check if two nodes are equal """
        return self.state == other.state

    def __lt__(self, other):
        """ Check if the cost of the current node is less than the cost of the other node """
        return self.cost + self.heuristic < other.cost + other.heuristic

    def __gt__(self, other):
        """ Check if the cost of the current node is greater than the cost of the other node """
        return self.cost + self.heuristic > other.cost + other.heuristic

    def __le__(self, other):
        """ Check if the cost of the current node is less than or equal to the cost of the other node """
        return self.cost + self.heuristic <= other.cost + other.heuristic

    def __ge__(self, other):
        """ Check if the cost of the current node is greater than or equal to the cost of the other node """
        return self.cost + self.heuristic >= other.cost + other.heuristic

    def __ne__(self, other):
        """ Check if two nodes are not equal """
        return self.state != other.state

    def __hash__(self):
        """ Hash the node to be used in the set or dictionary """
        return hash(self.state)

    def __str__(self):
        """ Print the node in the required format """
        return f"Node({self.state}, {self.parent}, {self.cost}, {self.heuristic})"


class AStar:
    def __init__(self, start_state, goal_state, data, heuristic_data):
        """ Initialize the A* Algorithm with the start state, goal state, state space and heuristic values """
        self.start_state = start_state
        self.goal_state = goal_state
        self.data = data
        self.heuristic_data = heuristic_data
        self.frontier = []
        self.explored = []
        self.path = []
        self.cost = 0
        self.nodes_expanded = 0
        self.max_search_depth = 0
        self.max_frontier_size = 0

    def search(self):
        """ A* Algorithm to search for the goal state """
        # Add the start state to the frontier
        self.frontier.append(
            Node(self.start_state, None, 0, self.heuristic_data[self.start_state]))

        # Loop until the frontier is empty
        while self.frontier:
            # Sort the frontier according to the cost
            self.frontier.sort()

            # Get the node with the lowest cost
            current_node = self.frontier.pop(0)

            # Add the current node to the explored list
            self.explored.append(current_node)

            # Check if the current node is the goal state
            if current_node.state == self.goal_state:
                self.nodes_expanded += 1
                self.path.append(current_node)
                self.cost = current_node.cost
                self.max_search_depth = current_node.cost
                self.max_frontier_size = len(self.frontier)
                return True

            # Expand the current node
            self.expand(current_node)

            # Update the max frontier size
            self.max_frontier_size = max(
                self.max_frontier_size, len(self.frontier))

        # Return False if the goal state is not found
        return False

    def expand(self, current_node):
        """ Expand the current node to get the next nodes """
        # Increment the number of nodes expanded
        self.nodes_expanded += 1

        # Get the next states from the current state
        next_states = self.data[current_node.state]

        # Loop through the next states
        for next_state in next_states:
            # Create a new node
            new_node = Node(next_state[0], current_node, current_node.cost +
                            next_state[1], self.heuristic_data[next_state[0]])

            # Check if the new node is in the explored list
            if new_node in self.explored:
                continue

            # Check if the new node is in the frontier
            if new_node in self.frontier:
                # Get the index of the node in the frontier
                index = self.frontier.index(new_node)

                # Check if the new node has a lower cost
                if new_node.cost < self.frontier[index].cost:
                    # Replace the node in the frontier with the new node
                    self.frontier[index] = new_node
            else:
                # Add the new node to the frontier
                self.frontier.append(new_node)

    def get_path(self):
        """ Get the path from the start state to the goal state """
        # Get the last node in the path
        current_node = self.path[-1]

        # Loop until the current node is the start state
        while current_node.state != self.start_state:
            # Add the current node to the path
            self.path.append(current_node.parent)

            # Get the parent of the current node
            current_node = current_node.parent

        # Reverse the path
        self.path.reverse()

        # Return the path
        return self.path

    def print_path_states(self):
        """ Print the path states in the format required by the assignment """
        # Get the path
        path = self.get_path()

        # Return the path states
        for i in path:
            if i.state != self.goal_state:
                print(i.state, end=' => ')
        print(self.goal_state)
        print()

    def get_explored_states(self):
        """ Return the explored states """
        # Return the explored states
        return [i.state for i in self.explored]


if __name__ == '__main__':
    # Create an AStar object
    astar = AStar(start_state[0], goal_state[0], data, heuristic_data)

    # Search for the goal state
    found = astar.search()

    # Print the results
    if found:
        print()
        print('States Visited =', astar.get_explored_states())
        print('Found path of length:', astar.nodes_expanded,
              'with total cost:', astar.cost)
        astar.print_path_states()
    else:
        print('Path not found!')
