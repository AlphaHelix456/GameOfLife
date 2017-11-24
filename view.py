'''
Created on Nov 22, 2017

@author: NeilShah-MacBookPro
'''

# Executable

from tkinter import Tk, Frame, TOP

import controller

# Construct a root window
root = Tk()
root.title('Game of Life')
root.protocol('WM_DELETE_WINDOW', quit)

# Place buttons at the top of the window
frame = Frame(root)
controller.start_button(frame, text = 'START')
controller.stop_button(frame, text = 'STOP')
controller.reset_button(frame, text = 'RESET')

frame.pack(side=TOP)

if __name__ == '__main__':
    controller.repeater(root)
    root.mainloop()