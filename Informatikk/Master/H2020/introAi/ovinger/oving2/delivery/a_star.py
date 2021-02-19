from Map import Map_Obj

# Class for holding the nodes
class Node():

    # Initialize with parent and position
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    # Getter for parent
    def get_parent(self):
        return self.parent

    # Getter for position
    def get_pos(self):
        return self.pos

    # Setter for the h-value. Calculated using Manhattan distance
    def set_h(self, goal):
        self.h = abs(goal[0] - self.pos[0]) + abs(goal[1] - self.pos[1])

    # Setter for the g-value. Calculated from parent's g and current cell-value.
    def set_g(self, maze):
        self.g = self.parent.get_g() + int(maze.get_cell_value(self.pos))

    # Getter for f-value
    def get_f(self):
        return self.f
    
    # Getter for h-value
    def get_h(self):
        return self.h
    
    # Getter for g-value
    def get_g(self):
        return self.g

    # Setter for f-value. Calculated with f = g + h
    def set_f(self):
        self.f = self.g + self.h

class A_star():

    # Initialize A_star with map, task, goal, current node, start node and open and closed lists.
    def __init__(self, task):
        self.map = Map_Obj(task)
        self.task = task
        self.goal = self.map.get_goal_pos()

        self.current_node = None
        # Create start node
        self.start = Node(self.map.get_start_pos(), None)
        # Set start node f and h value
        self.start.set_h(self.goal)
        self.start.set_f()
        self.open_list = set([self.start])
        self.closed_list = []
        self.path = []

    def solve(self):
        print(f'Solving task {self.task}')
        while len(self.open_list) > 0: # As long as open_list has childs, loop trough
            self.current_node = self.get_lowest_f_node() # Get the node with lowest f-value
            self.open_list.remove(self.current_node) # Remove the node from the open list
            self.closed_list.append(self.current_node.get_pos()) # Add the node to the closed list

            # Color all explored nodes yellow
            if self.current_node.get_pos() != self.start.get_pos() and self.current_node.get_pos() != self.goal and self.map.get_cell_value(self.current_node.get_pos()) <= 1:
                self.map.set_cell_value(self.current_node.get_pos(), "I")

            # If current node are goal node, we construct the path and break out of loop
            if self.current_node.get_pos() == self.goal:
                self.construct_path()
                break
            
            # Generate children for current_node
            children = self.generate_children(self.current_node)

            # Loop thorugh children and add to open list if position is not explored already.
            for child in children:
                if child.get_pos() not in self.closed_list:
                    self.open_list.add(child)
        
        # return the path
        return self.path

    def construct_path(self):
        tmpNode = self.current_node.get_parent()
        # Backtrack from goal to start to construct the path
        while tmpNode.get_parent() != None:
            self.path.append(tmpNode.get_pos())
            self.map.set_cell_value(tmpNode.get_pos(), "P")
            tmpNode = tmpNode.get_parent()
    
    def show_map(self):
        # Show the map
        self.map.show_map()
    
    def get_lowest_f_node(self):
        # Return the node with lowest f-value
        return min(self.open_list, key = lambda x: x.f)
    
    def generate_children(self, parent):
        children = []
        # Explore all neighbours of 'parent'. (up, down, left, right)
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            # Create a new node with that position
            child = Node([parent.get_pos()[0] + direction[0], parent.get_pos()[1] + direction[1]], parent)
            # If the node is not a wall ...
            if self.map.get_cell_value(child.get_pos()) != -1:
                # ... set h, g and f values on the child ...
                child.set_g(self.map)
                child.set_h(self.goal)
                child.set_f()
                # ... and append the child to children-list
                children.append(child)
        # return the children
        return children


def main():
    # Solve task 1
    a_star1 = A_star(1)
    a_star1.solve()
    
    # Solve task 2
    a_star2 = A_star(2)
    a_star2.solve()

    # Solve task 3
    a_star3 = A_star(3)
    a_star3.solve()

    # Solve task 4
    a_star4 = A_star(4)
    a_star4.solve()

    # Show maps
    a_star1.show_map()
    a_star2.show_map()
    a_star3.show_map()
    a_star4.show_map()

if __name__ == '__main__':
    main()