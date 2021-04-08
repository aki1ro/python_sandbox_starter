import os
import time
import subprocess as sp


def gather(f):
   x = sp.check_output(f'tree -f "//" | grep {f}', shell=True)
   x = str(list(x)).split('\n')
   print(x)


gather("Enter filename here to search:")