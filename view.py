'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''

# Executable

from tkinter import Tk, Frame, TOP, BOTTOM

import controller

# Construct a root window
root = Tk()
root.title('The Game of Life')
root.protocol('WM_DELETE_WINDOW', quit)

# Place buttons at the top of the window
frame = Frame(root)
frame.pack(side=TOP)
controller.start_button(frame, text = 'START')
controller.stop_button(frame, text = 'STOP')
controller.reset_button(frame, text = 'RESET')
controller.generation_label(frame, text = 'GENERATION: 0')
controller.grid_simulation_canvas(root, 1000, 1000).pack(side = BOTTOM, expand = True)

if __name__ == '__main__':
    controller.repeater(root)
    root.mainloop()