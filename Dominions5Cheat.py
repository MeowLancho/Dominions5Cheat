import pymem
from pymem import *

def WriteIntPerls():
    py_ref = Pymem("Dominions5.exe")
    py_ref.read_int(py_ref.base_address + 0x25D73DA)
    py_ref.write_int(py_ref.base_address + 0x25D73DA, 150000)
    py_ref.read_int(py_ref.base_address + 0x25D73DA)
if __name__ == "__main__":
    WriteIntPerls()
