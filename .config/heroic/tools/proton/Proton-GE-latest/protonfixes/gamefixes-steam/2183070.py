""" Game fix for Tokyo Necro
"""

from protonfixes import util

def main():
    """ installs xact, disable ESYNC, disable FSYNC
    """

    # Fixes crash after typing then entering or clicking `search` within the game's terminal menu
    util.protontricks('xact')
    # Fixes hanging after typing then entering or clicking `search` within the game's terminal menu
    util.disable_esync()
    util.disable_fsync()
    # Fixes audio not playing for in-game videos
    util.disable_protonmediaconverter()
