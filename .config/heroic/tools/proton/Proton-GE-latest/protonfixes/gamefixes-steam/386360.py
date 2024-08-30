""" Game fix for Smite
"""
#pylint: disable=C0103

import glob
import os
import subprocess
from protonfixes import util


def main():
    """ Fix EAC location in smite
    """
    install_dir = glob.escape(util.get_game_install_path())

    # Fix EAC incorrect location:
    if not os.path.exists(install_dir + '/Win64/EasyAntiCheat/easyanticheat_x64.so'):
        subprocess.call(['ln', '-s', install_dir + '/EasyAntiCheat/easyanticheat_x64.so', install_dir + '/Win64/EasyAntiCheat/'])

    if not os.path.exists(install_dir + '/Win32/EasyAntiCheat/easyanticheat_x86.so'):
        subprocess.call(['ln', '-s', install_dir + '/EasyAntiCheat/easyanticheat_x86.so', install_dir + '/Win32/EasyAntiCheat/'])
