""" Game fix for YOU and ME and HER: A Love Story
"""

from protonfixes import util

def main():
    """ install xact, disable esync, disable fsync
    """

    # Fixes the game from crashing or hanging during intro
    util.protontricks('xact')
    util.disable_esync()
    util.disable_fsync()
    # Fixes audio not playing for in-game videos
    util.disable_protonmediaconverter()
