import os.path
from datetime import datetime
from time import time, ctime
import sys

print(os.path.dirname("python-education/python-basics"))
print(sys.version)

t = time()
print(ctime(t))

PYCON_DATE = datetime(year=2022, month=2, day=22, hour=4)
countdown = PYCON_DATE - datetime.now()
print(f"Deadline for task: {countdown}")
