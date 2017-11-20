'''
Created on Nov 20, 2017

@author: NeilShah-MacBookPro
'''

class Cell:
    def __init__(self, x: int, y: int):
        self.location = (x, y)
        self.populated = False
        self.neighbors = get_neighbors(self.location)
    
    def get_location(self) -> (int, int):
        return self.location
    
    def is_populated(self) -> bool:
        return self.populated
    
def get_neighbors(location: (int, int)) -> [Cell]:
    neighbors = []
    x, y = location
    for x_coor in range(x - 1, x + 2):
        for  y_coor in range(y -1, y + 2):
            if (x_coor, y_coor) != location:
                neighbors.append(Cell(x, y))
    return neighbors