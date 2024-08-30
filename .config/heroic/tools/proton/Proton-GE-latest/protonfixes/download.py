""" Module with helper functions to download from file-hosting providers
"""

import os
import hashlib
import urllib.request
import http.cookiejar


GDRIVE_URL = 'https://drive.google.com/uc?id={}&export=download'
HASH_BLOCK_SIZE = 65536


def get_filename(headers: list) -> str:
    """ Retrieve a filename from a request headers via Content-Disposition
    """
    content_disp = [x for x in headers if x[0] == 'Content-Disposition'][0][1]
    raw_filename = [x for x in content_disp.split(';') if x.startswith('filename=')][0]
    return raw_filename.replace('filename=', '').replace('"', '')


def gdrive_download(gdrive_id: str, path: str) -> None:
    """ Download a file from gdrive given the fileid and a path to save
    """
    url = GDRIVE_URL.format(gdrive_id)
    cjar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=10) as resp:
        confirm_cookie = [x for x in resp.getheaders() if
                        (x[0] == 'Set-Cookie'
                        and x[1].startswith('download_warning'))][0][1]
    confirm = confirm_cookie.split(';')[0].split('=')[1]

    req = urllib.request.Request(f'{url}&confirm={confirm}')
    with urllib.request.urlopen(req, timeout=10) as resp:
        filename = get_filename(resp.getheaders())
        with open(os.path.join(path, filename), 'wb') as save_file:
            save_file.write(resp.read())


def sha1sum(filename: str) -> str:
    """ Computes the sha1sum of the specified file
    """
    if not os.path.isfile(filename):
        return ''
    hasher = hashlib.sha1()
    with open(filename, 'rb') as hash_file:
        buf = hash_file.read(HASH_BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = hash_file.read(HASH_BLOCK_SIZE)
    return hasher.hexdigest()
