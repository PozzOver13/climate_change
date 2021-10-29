import os
import inspect

# Paths
PATH_GENERAL = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PATH_REPO = os.path.dirname(os.path.dirname(PATH_GENERAL))
PATH_SRC = os.path.join(PATH_REPO, 'src')
PATH_TEST = os.path.join(PATH_REPO, 'test')
PATH_DATA_RAW = os.path.join(PATH_REPO, 'data', 'raw')
PATH_DATA_OUTPUT = os.path.join(PATH_REPO, 'data', 'output')


