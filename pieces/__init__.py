# With inspiration from answers to code from StackOverflow
# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder

# __all__ = []
#
# import os
# for module in os.listdir(os.path.dirname(__file__)):
#     if module in ('__init__.py', 'piece.py') or module[-3:] != '.py':
#         continue
#     __all__.append(module[:-3])
# print(__all__)
# del module
# del os

# Was only importing module namespace and not the classes.

from .bishop import Bishop
from.king import King
from .knight import Knight
from .pawn import Pawn
from.queen import Queen
from .rook import Rook
