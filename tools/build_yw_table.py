"""Build a Python script for the yw-table distribution.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the pywriter package.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/yw-table
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../PyWriter/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}yw_table_.py'
TARGET_FILE = f'{BUILD}yw_table.py'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvretablexlib', '../src/', copyPyWriter=False)
    inliner.run(TARGET_FILE, TARGET_FILE, 'nvmatrixlib', '../src/', copyPyWriter=False)
    inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../src/', copyPyWriter=False)
    print('Done.')


if __name__ == '__main__':
    main()
