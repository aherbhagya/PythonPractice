#!/usr/bin/python
import re

# \   Used to drop the special meaning of character
#     following it (discussed below)
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One ore more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs

# function compile

p=re.compile('[a-e]')

print p.findall(" are you happy with my program and are you really intersted")
