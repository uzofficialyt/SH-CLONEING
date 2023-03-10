import os, sys

os.system('xdg-open https://github.com/Mdshadhinali')

try:

    __import__("SHADHIN.cpython-311.opt-2.pyc").menu()

except Exception as e:

    exit(str(e))

