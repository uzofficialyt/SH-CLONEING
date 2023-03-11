
import os, sys

os.system("git pull")

try:

    __import__("SHADHIN.cpython-311.opt-2.pyc").Main()

except Exception as e:

    exit(str(e))
