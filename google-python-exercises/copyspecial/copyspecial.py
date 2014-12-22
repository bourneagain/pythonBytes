#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

#get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
#copy_to(paths, dir) given a list of paths, copies those files into the given directory
#zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile

			
def get_special_paths(dir):
     op=[]
     filenames=os.listdir('.')
     for files in filenames:
        pattern=re.search(r'__[a-zA-Z]+__',files)
        if pattern:
           op.append(os.path.abspath(files))
     return op
def copy_to(paths, dir):
    for file in paths:
        print "file to cpy is " + file
        if not os.path.isdir(file):
            shutil.copy(file,dir)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  if args[0] == ".":
     print get_special_paths(args[0])


  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    copy_to(get_special_paths('.'),todir)
    del args[0:2]
  
  sys.exit()
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
     
    
if __name__ == "__main__":
  main()
