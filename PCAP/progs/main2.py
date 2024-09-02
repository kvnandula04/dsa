import os
from sys import path

# Get the absolute path to the directory where the python file is
dir_path = os.path.dirname(os.path.realpath(__file__))

# Append the packages directory to the system path
path.append(os.path.join(dir_path, "..", "packages/pack.zip"))


for p in path:
    print(p)

import extra.good.best.sigma as sig
import extra.good.best.tau as tau

print(sig.FunS())
print(tau.FunT())
