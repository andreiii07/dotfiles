""" Game fix for Titanfall 2
"""
#pylint: disable=C0103

import os
import subprocess
import glob
from protonfixes import util

def main():
    """ Allow -northstar option to work
    """
    # Define game directory
    install_dir = glob.escape(util.get_game_install_path())

    # Restore original titanfall2.exe if NorthstarLauncher.exe was previously symlinked
    if os.path.isfile(install_dir + '/Titanfall2.exe.bak'):
        subprocess.run(['mv', 'Titanfall2.exe.bak', 'Titanfall2.exe'], check=False)
