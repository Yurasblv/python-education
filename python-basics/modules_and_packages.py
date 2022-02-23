import re

find_members = []
for f in dir(re):
    if "find" in f:
        find_members.append(f)
