#!/usr/bin/env python

from sys import argv

script, textfile = argv

txtobj = open(argv[1], 'r')

intostring = txtobj.read()

words = (((((intostring.replace('\n\n\t',' ')).replace('\n\t',' '))
           .replace('\n\n',' ')).replace('\n',' '))
         .replace(' - ',' ')).split()

print len(words)

txtobj.close()
