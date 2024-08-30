""" Game fix for Spider-Man: Shattered Dimensions
"""
#pylint: disable=C0103
#
from protonfixes import util

def main():
    """ installs d3dx9_43, xact
    """

    # https://steamcommunity.com/app/231990/discussions/0/3198117312260185786/#c3470604115208907456
    util.protontricks('d3dx9_43')
    util.protontricks('xact')
