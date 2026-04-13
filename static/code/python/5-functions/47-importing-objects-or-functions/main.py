# 3 types of import:

# localized import
from module import method

method()


import module

module.method()


from module import brew as brr

brr()


# stdlib
# from datetime import datetime

# submodule
# from module.submodule import method

#  module/
#      submodule/
#          method.py


# all import
# import recipies.flavours

# print(recipies.flavours.elachi_chai())


# named import
from recipies.flavours import adrak_chai, elachi_chai, ginger_chai

print(ginger_chai())


# relative import
from .recipies import flavours  # .. for one level up

print(flavours.adrak_chai())


# import all (avoid)
from .recipies.flavours import *

print(elachi_chai())


# from py 3.3/4 we dont really need to use __init__.py
