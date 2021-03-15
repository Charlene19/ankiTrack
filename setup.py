from cx_Freeze import setup, Executable
import sys


build_exe_options = {"includes": ["tkinter"]}

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# On appelle la fonction setup
setup(
    name="AyseProg",
    version="1",
    description="Tracker",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)
