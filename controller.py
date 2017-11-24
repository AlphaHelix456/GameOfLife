'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''
from tkinter import Button

import model

# The view calls these functions to place buttons in a frame
def start_button(parent, **config) -> Button:
    return Button(parent, command = '', **config)

def stop_button(parent, **config) -> Button:
    return Button(parent, command = '', **config)

def reset_button(parent, **config) -> Button:
    return Button(parent, command = '', **config)

# The repeater calls itself every 1000 milliseconds
# The grid updates itself every second
# Calls functions from the model to update and display the grid
def repeater(root) -> None:
    root.after(1000, repeater, root)