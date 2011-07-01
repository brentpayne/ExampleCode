'''
Created on Aug 5, 2010

@author: brent
'''

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
output='def'

#This example looks for a word following a hyphen:

m = re.search('(?<=-)\w+', 'spam-egg')
m.group(0)
output='egg'

re.match("c", "abcdef")  # No match
re.search("c", "abcdef") # Match

pattern = "match.*this\s[Bb]itch(?:es)?" 
prog = re.compile(pattern)
result = prog.match(string)
