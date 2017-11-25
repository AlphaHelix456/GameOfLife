'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''

# Executable

from tkinter import Tk, Frame, TOP, BOTTOM, LEFT, BOTH

import controller

# Construct a root window
root = Tk()
root.title('The Game of Life')
root.protocol('WM_DELETE_WINDOW', quit)

# Place buttons at the top of the window
frame = Frame(root)
frame.pack(side=TOP)
controller.start_button(frame, text = 'START').pack(side = LEFT)
controller.stop_button(frame, text = 'STOP').pack(side = LEFT)
controller.reset_button(frame, text = 'RESET').pack(side = LEFT)
controller.generation_label(frame, text = 'GENERATION: 0').pack(side = LEFT)
controller.grid_simulation_canvas(root, width = 1000, height = 1000).pack(side = BOTTOM, fill = BOTH, expand = True)

if __name__ == '__main__':
    controller.repeater(root)
    root.mainloop()