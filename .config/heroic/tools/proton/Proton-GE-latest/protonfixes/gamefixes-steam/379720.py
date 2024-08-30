""" Game fix for Doom 2016
"""
#pylint: disable=C0103
import os
import shutil
import urllib.request
import zipfile

from protonfixes import util


def main():
    """ Enable preload options
    """

    # Enable preload options
    util.append_argument('+r_renderAPI 1')

    installpath = os.path.abspath(os.getcwd())
    url = "https://github.com/Riesi/CChromaEditor/files/2277158/CChromaEditorLibrary.zip"

    if not os.path.isfile(os.path.join(installpath, 'CChromaEditorLibrary.dll.bak')):
        urllib.request.urlretrieve (url, "CChromaEditorLibrary.zip")
        shutil.move(os.path.join(installpath, 'CChromaEditorLibrary.dll'),
                    os.path.join(installpath, 'CChromaEditorLibrary.dll.bak'))
        with zipfile.ZipFile("CChromaEditorLibrary.zip", "r") as zip_ref:
            zip_ref.extractall(installpath)
