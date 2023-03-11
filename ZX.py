import os, sys

os.system("git pull")

try:

    __import__("SHADHIN.cpython-311").Main()

except Exception as e:

    exit(str(e))
