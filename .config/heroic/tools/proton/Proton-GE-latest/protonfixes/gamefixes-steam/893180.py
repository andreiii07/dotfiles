""" Game fix Catherine Classic
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.protontricks('directshow')
    util.protontricks('cinepak')
    util.protontricks('lavfilters')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dcompiler_47')
    util.disable_protonmediaconverter()
