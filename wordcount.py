#!/usr/bin/env python

'''
This software is copyright 2013 by Daniel Ellen (dhe) and icensed under
the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of
the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
'''

from sys import argv

script, textfile = argv

txtobj = open(argv[1], 'r')

intostring = txtobj.read()

words = (((((intostring.replace('\n\n\t',' ')).replace('\n\t',' '))
           .replace('\n\n',' ')).replace('\n',' '))
         .replace(' - ',' ')).split()

print len(words)

txtobj.close()
