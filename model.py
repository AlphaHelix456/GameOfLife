'''
Created on Nov 20, 2017

@author: NeilShah-MacBookPro
'''

# Every cell interacts with its eight neighbors
# At each generation, the following transitions occur simultaneously :
# Any live cell with fewer than 2 alive neighbors dies
# Any live cell with 2 or 3 alive neighbors stays alive
# Any live cell with more than 3 alive neighbors dies
# Any dead cell with exactly 3 alive neighbors dies


class Cell:
    def __init__(self, x: int, y: int):
        self._location = (x, y)
        self._populated = False
    
    def get_location(self) -> (int, int):
        return self._location
    
    def is_populated(self) -> bool:
        return self._populated
    
    def set_new_state(self, state: bool):
        self._populated = state
        
class Grid:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._cells = create_grid(width, height)
        
    def get_cells(self) -> [[Cell]]:
        return self._cells
    
    def next_generation(self):
        new_states = []
        for row in range(self._width):
            state_sublist = []
            for col in range(self._height):
                cell = self._cells[row][col]
                cell_neighbors = get_neighbors(self._cells, cell.get_location())
                state_sublist.append(advance_state(cell, cell_neighbors))
            new_states.append(state_sublist)
        self._cells = update_cell_states(self._cells, new_states)
def get_neighbors(grid: [[Cell]], location: (int, int)) -> [Cell]:
    neighbors = []
    x, y = location
    for x_coor in range(x - 1, x + 2):
        for  y_coor in range(y - 1, y + 2):
            if (x_coor, y_coor) != location and cell_in_bounds(x_coor, y_coor, len(grid), len(grid[x_coor])):
                neighbors.append(grid[x_coor][y_coor])
    return neighbors

# Returns number of neighboring cells that are populated 
def get_alive_neighbor_count(neighbors: [Cell]) -> int:
    return sum([1 for neighbor in neighbors if neighbor.is_populated()])

# Cell is either populated or unpopulated
def advance_state(cell: Cell, neighbors: [Cell]) -> bool:
    alive_neighbors = get_alive_neighbor_count(neighbors)
    if cell.is_populated():
        return alive_neighbors == 2 or alive_neighbors == 3
    return alive_neighbors == 3 

def update_cell_states(new_states: [[bool]], grid: [[Cell]]) -> [[Cell]]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col].set_new_state(new_states[row][col])
        
def create_grid(width: int, height: int) -> [[Cell]]:
    grid = []
    for x_coor in range(width):
        grid.append([Cell(x_coor, y_coor) for y_coor in range(height)])
    return grid

def cell_in_bounds(x_coor: int, y_coor: int, width: int, height: int):
    return 0 <= x_coor < width and 0 <= y_coor < height