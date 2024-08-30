""" Game fix for JUMP FORCE
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.replace_command('JUMP_FORCE.exe', 'JUMP_FORCE/Binaries/Win64/JUMP_FORCE-Win64-Shipping.exe')
    util.append_argument('-eac-nop-loaded')

    util.protontricks('hidewineexports=enable')
