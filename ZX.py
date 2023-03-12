import os, sys

os.system('git pull')

try:

    __import__("SHADHIN").rsbuy()

except Exception as e:

    exit(str(e))
