""" Forza Horizon 4
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    # Replace launcher with game exe in proton arguments
    util.protontricks('vcrun2019')
