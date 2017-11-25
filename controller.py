'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''
from tkinter import Button, Label, Canvas

import model
generation = None
canvas = None

# The view calls these functions to place buttons in a frame
def start_button(parent, **config) -> Button:
    return Button(parent, command = model.start, **config)

def stop_button(parent, **config) -> Button:
    return Button(parent, command = model.stop, **config)

def reset_button(parent, **config) -> Button:
    return Button(parent, command = model.reset, **config)

def generation_label(parent, **config) -> Label:
    global generation
    generation = Label(parent, **config)
    return generation

def grid_simulation_canvas(parent, **config) -> Canvas:
    global canvas
    canvas = Canvas(parent, **config)
    canvas.bind('<Button-1>', model.mouse_click)
    return canvas

# The repeater calls itself every 1000 milliseconds
# The grid updates itself every second
# Calls functions from the models to update and display the grid
def repeater(root) -> None:
    model.update_grid()
    model.display_grid()
    root.after(1000, repeater, root)