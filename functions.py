from tkinter import Tk
import os
import sys

def restart_program():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

def on_closing():
    window.destroy()
    exit()

window = Tk()