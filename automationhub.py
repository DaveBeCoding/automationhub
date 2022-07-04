#!/usr/bin/env python

from alive_progress import alive_bar
from time import sleep
from turtle import pd
from git import Repo
import banner
import sys
import os

# separate module(s)
#
# sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from vars import *


def dotGitExist() -> bool:
    ''' Check for the existance of a .git dir '''
    count = ONE_HUNDRED - ONE_HUNDRED
    if count > MAX_COUNT:
        print("not found")
        sys.exit(EXIT_CODE)

    try:
        if os.path.isdir(CWD):
            print(".git found in -> "
                  + CWD)
            # call gitupdater
            gitupdater(CWD)
        else:
            if os.path.isdir(UP_DIR):
                os.chdir(CHANGE_UP)
                new_location = os.getcwd()
                print('.git found in -> '
                      + str(new_location))
                # call gitupdater
                gitupdater(new_location)
            elif os.path.isdir(UP_DIR_X_TWO):
                os.chdir(CHANGE_UP_SQUARE)
                location = os.getcwd()
                print('.git found in -> '
                      + str(location))
                # call gitupdater
                gitupdater(location)
            else:
                # work on logic of this section next <-
                dir = next(os.walk(WALK_NEXT))[COUNT_ONE]
                dir_str = ''.join(dir)
                os.chdir('./'+dir_str)
                count += COUNT_ONE
                dotGitExist()
    except:
        print(FAIL_LOCATE_DIR)


def progressor():
    '''Terminal status'''
    with alive_bar(ONE_HUNDRED) as bar:
        for i in range(ONE_HUNDRED):
            sleep(SLEEPY_TIME)
            bar()

    # using bubble bar and notes spinner
    with alive_bar(ONE_HUNDRED + ONE_HUNDRED, bar='bubbles',
                   spinner='notes2') as bar:
        for i in range(ONE_HUNDRED + ONE_HUNDRED):
            sleep(SLEEPY_TIME)
            bar()


def gitupdater(git_path) -> str:
    '''automate updating repo dir'''
    try:
        progressor()
        repo = Repo(git_path)
        repo.git.pull(GIT_PULL)
        repo.git.add([GIT_ADD])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name=REMOTE_NAME)
        origin.push()
        progressor()
        os.system(SYSTEM_CLEAR)
        banner.print_banner("RUN COMMAND -> deactivate")


    except:
        print(FAIL_EXCEPTION)


def current_path():
    os.getcwd()


def main():
    '''Main, call functions to perform github automation .:. Example [g_updater.py "write git message"...]'''
    os.system(SYSTEM_CLEAR)
    # import pdb; pdb.set_trace()
    if len(COMMIT_MESSAGE) < COUNT_ONE:
        input('example input -> Automationhub.py "your message to github"')
        sys.exit(EXIT_CODE)
    progressor()
    dotGitExist()


if __name__ == '__main__':
    main()

# test funct(s) in separate files
# use this only as drive (main)

#TEST CREATING A SUBPROCESS TO DEACTIVATE VENV
#TEST BASH SCRIPT WITH ALIAS TO DEACTIVATE VENV
#TEST COMBO OF BOTH
#GOAL NO USER INTERACTION WITH SCRIPT ONCE GIT MSG HAS BEEN INPUT
