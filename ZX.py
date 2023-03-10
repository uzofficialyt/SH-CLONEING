import os, sys

os.system('xdg-open https://github.com/Mdshadhinali')

try:

    __import__("SHADHIN").menu()

except Exception as e:

    exit(str(e))

