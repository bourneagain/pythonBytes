#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
import sys,pprint
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  op=[]
  yearCheck=0
  nameDict={}
  with open(filename) as f:
   for line in f:
     if not yearCheck:
        yearMatch=re.search(r'Popularity\sin\s([0-9]{4})',line)
        if yearMatch:
           op.append(yearMatch.group(1))
           yearCheck=1
           continue
     rankAndName=re.search(r'<tr\salign="right"><td>([0-9]+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>',line)
     if rankAndName:
        rank=rankAndName.group(1)
        name1=rankAndName.group(2)
        name2=rankAndName.group(3)
        try:
           if nameDict[name1] > rank:
               nameDict[name1]=rank
        except:
           nameDict[name1]=rank
        try:
           if nameDict[name2] > rank:
               nameDict[name2]=rank
        except:
           nameDict[name2]=rank

  for name,rank in nameDict.iteritems():
      op.append(name+' '+rank)
  return op

import time
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for files in range(0,len(args)):
      filename=args[0]
      if summary:
         with open(filename+'.summary','w') as f:
              f.write('\n'.join(extract_names(filename))+'\n')
         print "COMPLETED WRITING for "+filename
      else:
         print extract_names(filename)
         print "COMPLETED for "+filename
      time.sleep(1)     
      del args[0]
  
if __name__ == '__main__':
  main()
