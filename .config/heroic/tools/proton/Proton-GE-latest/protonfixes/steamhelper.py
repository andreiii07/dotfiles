""" The Steamhelper allows the installation of Steam apps
"""

import os
import re
import shutil
import subprocess
import time


libpaths = []
REGEX_LIB = re.compile(r'"path"\s*"(?P<path>(.*))"')
REGEX_STATE = re.compile(r'"StateFlags"\s*"(?P<state>(\d))"')
STEAM_DIRS = [
    "~/.steam/root", 
    "~/.steam/debian-installation", 
    "~/.local/share/Steam", 
    "~/.steam/steam"
]

def install_app(appid: str, delay: int = 1) -> None:
    """ Wait for the installation of an appid
    """
    _install_steam_appid(appid)
    while not _is_app_installed(appid):
        time.sleep(delay)

def _install_steam_appid(appid: str) -> None:
    """ Call steam URL
    """
    install_url = "steam://install/"+str(appid)
    if shutil.which("xdg-open"):
        subprocess.call(["xdg-open", install_url])
    elif shutil.which("gvfs-open"):
        subprocess.call(["gvfs-open", install_url])
    elif shutil.which("gnome-open"):
        subprocess.call(["gnome-open", install_url])
    elif shutil.which("kde-open"):
        subprocess.call(["kde-open", install_url])
    elif shutil.which("exo-open"):
        subprocess.call(["exo-open", install_url])

def _is_app_installed(appid: str) -> bool:
    """ Check if app is installed
    """
    libraries_path = _get_steam_libraries_path()

    # bypass no library path
    if len(libraries_path) == 0:
        return True

    is_installed = False
    for librarypath in libraries_path:
        appmanifest_path = _get_manifest_path(appid, librarypath)
        if os.path.exists(appmanifest_path):
            state = _find_regex_groups(appmanifest_path, REGEX_STATE, 'state')
            if(len(state)>0 and int(state[0])==4):
                is_installed = True
            break
    return is_installed

def _get_steam_libraries_path() -> list:
    """ Get Steam Libraries Path
    """
    if len(libpaths) == 0:
        for steampath in STEAM_DIRS:
            libfile = os.path.join(os.path.expanduser(steampath),"steamapps","libraryfolders.vdf")
            if os.path.exists(libfile):
                libpaths.append(_find_regex_groups(libfile, REGEX_LIB, 'path'))
                break
    return libpaths


def _get_manifest_path(appid: str, librarypath: str) -> str:
    """Get appmanifest path
    """
    return os.path.join(librarypath, "steamapps", f"appmanifest_{str(appid)}.acf")

def _find_regex_groups(path: str, regex: re.Pattern, groupname: str) -> list:
    """ Given a file and a regex with a named group groupname, return an
        array of all the matches
    """
    matches = []
    with open(path, encoding='ascii') as re_file:
        for line in re_file:
            search = regex.search(line)
            if search:
                matches.append(search.group(groupname))
    return matches
