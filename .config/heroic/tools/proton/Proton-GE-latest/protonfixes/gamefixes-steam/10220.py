""" Postal III
"""
#pylint: disable=C0103

from protonfixes import util

# Missing fonts for console and various UI
# grep -rh --include "*.res" '"name"' . | awk -F '"' '{print $4}' | awk '!visited[$0]++'
def main():
    util.protontricks('lucida')
    util.protontricks('courier')
    util.protontricks('verdana')
    util.protontricks('trebuchet')
    util.protontricks('arial')
    util.protontricks('tahoma')
