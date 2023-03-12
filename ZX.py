import os, sys

try:

    __import__("SHADHIN.cpython-311.so").rsbuy()

except Exception as e:

    exit(str(e))
