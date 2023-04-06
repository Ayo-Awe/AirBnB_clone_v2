#!/usr/bin/python3
"""Generate a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """This function generates a .tgz archive from the
    contents of the web_static folder and stores it in
    the version folder
    """
    date_format = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date_format}.tgz"
    local("mkdir -p versions")
    archive = local(f"tar -cvzf {file_path} web_static")

    if archive.failed:
        return None

    return file_path
