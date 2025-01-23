import os
import sys

def restart_program():
    python = sys.executable
    os.execv(python, [python] + sys.argv)
