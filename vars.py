from sys import argv
from os import getcwd

# GIT VARs
COMMIT_MESSAGE = ''.join(argv[1:])
GIT_ADD = '.'
GIT_PULL = 'origin'
REMOTE_NAME = GIT_PULL
FAIL_LOCATE_DIR ='Error locating .git dir'
FAIL_EXCEPTION = 'Error occured while pushing code'

# SYSTEM
UP_DIR = '../.git'
SYSTEM_CLEAR = "clear"
CWD = getcwd() + '/.git'
UP_DIR_X_TWO = '../../.git'

CHANGE_UP = '../'
CHANGE_UP_SQUARE = '../../'

# COUNTERS
SLEEPY_TIME = 0.03
ONE_HUNDRED = 100
MAX_COUNT = 3
COUNT_ONE = 1
EXIT_CODE = 0

# MAIN
WALK_NEXT = GIT_ADD

# move to modules dir


