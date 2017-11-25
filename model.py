'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''
from tkinter import Event, ALL
import logic
import controller

running = False
generation_count = 0

GRID_WIDTH = 30
GRID_HEIGHT = 30
grid = logic.Grid(GRID_HEIGHT, GRID_WIDTH)
    
def update_grid():
    global generation_count
    if running:
        grid.next_generation()
        generation_count += 1

def display_grid():
    controller.canvas.delete(ALL)
    
    grid.display(controller.canvas)
    
    controller.generation.config(text = 'GENERATION: ' + str(generation_count))

def mouse_click(event: Event):
    grid.handle_mouse_click(event.x, event.y, controller.canvas)

def start():
    global running
    running = True
    
def stop():
    global running
    running = False

    
def reset():
    global running, generation_count, grid
    running = False
    generation_count = 0
    grid = logic.Grid(GRID_WIDTH, GRID_HEIGHT)
    
    