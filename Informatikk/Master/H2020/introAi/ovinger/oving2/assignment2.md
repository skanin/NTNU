# Assignment 2

## Instructions

In my delivery, there are 2 files (along with the maps). `a_star.py` and `Map.py`. `Map.py` are the released map object, with some modifications to the coloring. `a_star.py` contains my implementation of the A* algorithm. It contains two classes, `Node` and `A_star`. `Node`-objects are positions in the map. `A_star` are the actual A* algortihm. It contains some functions, but the main one are `solve()`. All other functions are merely helper functions.

Upon creating a A_star object, you can input which task in the assignment you want to solve. E.g `a_star = A_star(1)`. To run the tasks, you simply have to run the file `a_star.py`, from the same directory as `Map.py` is located. I have set up so that all tasks are run simultaneously.

## Visulalizations

### Task 1 and 2 - with only walls

The green cells are the path my algorithm found, the yellow are all nodes that was explored.

<div style="display:flex; page-break-after: always"><figure><img src="task_1.png">
<figcaption>Task 1</figcaption></figure><figure><img src="task_2.png">
<figcaption>Task 2</figcaption></figure>
</div>

### Task 3 and 4 - with different cell values

In these tasks, I had to take the cell values into account. What I did was to just add `int(maze.get_cell_value(self.pos))` to the node's g-value.

The green cells are the path my algorithm found, the yellow are all nodes that was explored.

<div style="display:flex;"><figure><img src="task_3.png">
<figcaption>Task 3</figcaption></figure><figure><img src="task_4.png">
<figcaption>Task 4</figcaption></figure>
</div>
