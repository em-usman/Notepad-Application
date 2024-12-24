import cx_Freeze
import sys
import os

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

# Set the environment variables for Tcl and Tk
os.environ['TCL_LIBRARY'] = r"C:\\Users\\Umer_ali\\AppData\\Local\\Programs\\Python\\Python312\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\\Users\\Umer_ali\\AppData\\Local\\Programs\\Python\\Python312\\tcl\\tk8.6"

# Path to DLL files
dll_path = r"C:\\Users\\Umer_ali\\AppData\\Local\\Programs\\Python\\Python312\\DLLs"

executables = [cx_Freeze.Executable("app.py", base=base, icon="mainicon.ico")]

cx_Freeze.setup(
    name="Notepad Application",
    options={
        "build_exe": {
            "packages": ["tkinter", "os","re"],
            "include_files": [
                "mainicon.ico",
                os.path.join(dll_path, 'tcl86t.dll'),
                os.path.join(dll_path, 'tk86t.dll'),
                'icons2'
            ]
        }
    },
    version="0.1",
    description="Tkinter Application",
    executables=executables
)
