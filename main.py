import random


class Cell:
    x = y = 0
    wall = False
    visited=False
    def __init__(self, x=0, y=0, wall=True):
        self.x = x
        self.y = y
        self.wall = wall


class Map:
    map = []
    size = 0
    buffer = []

    def __init__(self, size):
        self.size = size
        for y in range(size):
            for x in range(size):
                self.map.append(Cell(x, y))

    def display(self):
        for y in range(self.size):
            cell_line = ""
            for x in range(self.size):
                cell_line += "  " if self.map[y *
                                              self.size + x].wall == False else "# "

            print(cell_line)


def depth_first_search(map):
    # random cell to start with
    start_cell_x = random.randrange(0, map.size)
    start_cell_y = random.randrange(0, map.size)
    # mark cell

    def mark_cell(x, y):
        neighbour_cells = []
        map.map[y*(map.size)+x].wall = False
        map.map[y*(map.size)+x].visited = True
        if x > 0:
            if not map.map[y*map.size+x-1].visited:
                neighbour_cells.append(map.map[y*map.size+x-1])
        if x < map.size-1:
            if not map.map[y*map.size+x+1].visited:
                neighbour_cells.append(map.map[y*map.size+x+1])
        if y > 0:
            if not map.map[(y-1)*map.size+x].visited:
                neighbour_cells.append(map.map[(y-1)*map.size+x])
        if y < map.size-1:
            if not map.map[(y+1)*map.size+x].visited:
                neighbour_cells.append(map.map[(y+1)*map.size+x])

        while len(neighbour_cells) > 0:
            next_cell_id=random.randrange(0, len(neighbour_cells),1)
            next_cell = neighbour_cells[next_cell_id]
            neighbour_cells.pop(next_cell_id)
            map.display()
            mark_cell(next_cell.x, next_cell.y)
    mark_cell(start_cell_x, start_cell_y)


def Start():
    map_size = 10
    map = Map(map_size)

    # algorithm
    depth_first_search(map)

    map.display()


Start()
