'''
Created on Nov 20, 2017

@author: NeilShah-MacBookPro
'''

class Cell:
    def __init__(self, x: int, y: int):
        self.location = (x, y)
        self.populated = False
    
    def get_location(self) -> (int, int):
        return self.location
    
    def is_populated(self) -> bool:
        return self.populated