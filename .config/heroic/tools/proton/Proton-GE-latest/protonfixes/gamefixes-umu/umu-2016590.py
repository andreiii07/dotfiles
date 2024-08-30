""" Game fix for Dark and Darker
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Installs wininet and urlmon in order to allow Blacksmith Launcher to properly install the game.
        
        This also has the side effect of breaking voip in DungeonCrawler.exe, so we add registry entries
        to only use native wininet and urlmon for Blacksmith.exe, and not DungeonCrawler.exe.
    """

    util.protontricks('wininet')
    util.protontricks('urlmon')

    util.regedit_add('HKEY_CURRENT_USER\\Software\\Wine\\AppDefaults\\DungeonCrawler.exe\\DllOverrides','wininet','REG_SZ','builtin')
    util.regedit_add('HKEY_CURRENT_USER\\Software\\Wine\\AppDefaults\\DungeonCrawler.exe\\DllOverrides','urlmon','REG_SZ','builtin')
