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
        self._neighbors = set_neighbors(self._location)
    
    def get_location(self) -> (int, int):
        return self._location
    
    def is_populated(self) -> bool:
        return self._populated
    
    def get_neighbors(self) -> [Cell]:
        return self._neighbors
    
def set_neighbors(location: (int, int)) -> [Cell]:
    neighbors = []
    x, y = location
    for x_coor in range(x - 1, x + 2):
        for  y_coor in range(y -1, y + 2):
            if (x_coor, y_coor) != location:
                neighbors.append(Cell(x, y))
    return neighbors

# Returns number of neighboring cells that are populated 
def get_alive_neighbor_count(cell: Cell) -> int:
    return sum([1 for neighbor in cell.get_neighbors() if neighbor.is_populated()])

# Returns True for populated, False for unpopulated
def advance_state(cell: Cell) -> bool:
    alive_neighbors = get_alive_neighbor_count(cell)
    if cell.is_populated():
        return alive_neighbors == 2 or alive_neighbors == 3
    return alive_neighbors == 3 