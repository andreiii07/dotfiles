""" Game fix for Dragon Age Inquisition
"""
#pylint: disable=C0103
from protonfixes import util

def main():
    """ Has Xinput patch in proton-wine
    """
    # Set SteamGameId so that non-steam versions can pick up steam-specific fixes in proton's wine code
    util.set_environment('SteamGameId','1222690')
