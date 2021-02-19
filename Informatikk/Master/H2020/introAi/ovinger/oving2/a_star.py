from Map import Map_Obj
import time

class Node():
    def __init__(self, pos=None, parent=None, children=None):
        self.pos = pos
        self.parent = parent
        self.children = children
        self.g = 0
        self.h = 0
        self.f = 0
    
    def get_children(self):
        return self.children
    
    def set_children(self, children):
        self.children = children
    
    def get_pos(self):
        return self.pos
    
    def get_parent(self):
        return self.parent

    def set_h(self, h):
        self.h = h
    
    def set_g(self, g):
        self.g = g
    
    def set_f(self, h, g):
        self.set_h(h)
        self.set_g(g)
        self.f = self.h + self.g

class A_star():
    def __init__(self, task):
        self.map = Map_Obj(task)
        self.goal = self.map.get_goal_pos()
        self.wall = -1

        start = Node(pos=self.map.get_start_pos())
        start.set_h(self.get_h(start))

        self.openList = set([start])
        self.closedList = []
        self.current_node = Node()
        self.path = []
        self.cost_mappings = {
            ' . ': 1,
            ' , ': 2,
            ' : ': 3,
            ' ; ': 4
        }
        self.allNodes = [self.current_node]
        self.last_node = self.current_node
    
    def solve(self, task=1):
        while len(self.openList) > 0:
            self.current_node = self.get_lowest_f_node()
            self.openList.remove(self.current_node)
            
            print(self.current_node.get_pos())

            self.closedList.append(self.current_node.get_pos())

            if self.current_node.get_pos() != self.get_start_node() and self.current_node.get_pos() != self.goal and self.map.get_cell_value(self.current_node.get_pos()) <= 1:
                self.map.set_cell_value(self.current_node.get_pos(), "I")


            if self.current_node.get_pos() == self.goal:
                tmpNode = self.current_node.get_parent()
                while tmpNode.get_parent() != None:
                    self.path.append(tmpNode.get_pos())
                    self.map.set_cell_value(tmpNode.get_pos(), "P")
                    tmpNode = tmpNode.get_parent()
                break

            self.current_node.set_children(self.generate_children(self.current_node))

            for child in self.current_node.get_children():
                
                if child.get_pos() in self.closedList:
                    print("Hey")
                    continue
                
                # g = child.get_parent().g + int(self.map.get_cell_value(child.get_pos()))
                # h = self.get_h(child)
                # child.set_f(h, g)
                self.openList.add(child)
            
        return self.path
    
    def show_map(self):
        self.map.show_map()

    def get_start_node(self):
        return self.map.start_pos

    def get_lowest_f_node(self):
        """
        lowest = 9999999
        current_lowest = Node()
        for node in self.openList:
            print(f'{node.f} - {node} - {node.get_pos()}')
            if node.f < lowest:
                current_lowest = node
                lowest = node.f
        """      

        return min(self.openList, key = lambda x: x.f)
        # return current_lowest

    def generate_children(self, node):
        tmp = []
        pos = node.get_pos()

        # Down
        if self.map.get_cell_value([pos[0] + 1, pos[1]]) != self.wall:
            if ([pos[0] + 1, pos[1]] in map(lambda x: x.get_pos(), self.allNodes)):
                tmp.append(filter(lambda x: x.get_pos() == [pos[0] + 1, pos[1]], self.allNodes))
            else:
                tmp.append(Node(pos=[pos[0] + 1, pos[1]], parent=node))

        # Right
        if self.map.get_cell_value([pos[0], pos[1] + 1]) != self.wall:
            if ([pos[0], pos[1] + 1] in map(lambda x: x.get_pos(), self.allNodes)):
                tmp.append(filter(lambda x: x.get_pos() == [pos[0], pos[1] + 1], self.allNodes)[0])
            else:    
                tmp.append(Node(pos = [pos[0], pos[1] + 1], parent = node))
        
        # Up
        if self.map.get_cell_value([pos[0] - 1, pos[1]]) != self.wall:
            if ([pos[0] - 1, pos[1]] in map(lambda x: x.get_pos(), self.allNodes)):
                tmp.append(filter(lambda x: x.get_pos() == [pos[0] - 1, pos[1]], self.allNodes)[0])
            else:
                tmp.append(Node(pos = [pos[0] - 1, pos[1]], parent = node))
        
        # Left
        if self.map.get_cell_value([pos[0], pos[1] - 1]) != self.wall:
            if ([pos[0], pos[1] - 1] in map(lambda x: x.get_pos(), self.allNodes)):
                tmp.append(filter(lambda x: x.get_pos() == [pos[0], pos[1] - 1], self.allNodes)[0])
            else:
                tmp.append(Node(pos=[pos[0], pos[1] - 1], parent=node))
            
        for child in tmp:
            pos = child.get_pos()

            g = int(self.map.get_cell_value(pos)) + child.get_parent().f
            h = self.get_h(child)
            child.set_f(h, g)

        return list(filter(lambda x: x.get_pos() not in self.closedList, tmp))
    
    def get_h(self, node, g=0):
        p1 = node.get_pos()[0]
        q1 = self.goal[0]
        p2 = node.get_pos()[1]
        q2 = self.goal[1]

        return ((q1-p1)**2 + (q2-p2)**2)**0.5
        #return abs(p1-p2) + abs(q1-q2)

    

a_star = A_star(3)

a_star.solve()

a_star.show_map()

# n = Node(pos=[27, 18], children=a_star.generate_children([27, 18]))

# print(n.get_parent())

# print(a_star.solve())

# mapp = Map_Obj(1)
# mapp.set_cell_value([40, 33], "Hei")
# mapp.show_map()