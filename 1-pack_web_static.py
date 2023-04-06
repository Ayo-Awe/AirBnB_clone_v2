#!/usr/bin/python3
"""Generate a .tgz archive from the
contents of the web_static folder and
store it in the versions folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """This function generates a .tgz archive from the
    contents of the web_static folder and stores it in
    the version folder
    """
    date_format = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date_format)
    local("mkdir -p versions")
    archive = local("tar -cvzf {} web_static".format(file_path))

    if archive.failed:
        return None

    return file_path
