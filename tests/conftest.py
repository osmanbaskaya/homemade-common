import sys
from os.path import abspath
from os.path import dirname

try:
    import homemade_common
except ModuleNotFoundError:
    repo_path = abspath(dirname(dirname(__file__)))
    sys.path.insert(1, repo_path)
    import homemade_common
