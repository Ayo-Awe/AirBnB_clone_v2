#!/usr/bin/python3
"""Deploy new archive releases
to web servers. Uploads the new archive
and configures the new release on the server
"""
from datetime import datetime
import os
from fabric.api import env, put, sudo, local

env.hosts = ["54.234.93.141", "34.207.154.98"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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


def do_deploy(archive_path):
    """Deploy new archive releases
        to web servers and configure the
        web servers for the new release
    """
    archive_name = os.path.basename(archive_path).split(".")[0]
    if not os.path.exists(archive_path):
        return False

    temp_archive, = put(local_path=archive_path, remote_path="/tmp")
    folder_name = "/data/web_static/releases/{}".format(archive_name)
    r1 = sudo("mkdir -p {}".format(folder_name))
    r2 = sudo("tar -xzvf {} -C {}".format(temp_archive, folder_name))
    r3 = sudo("mv {}/web_static/* {}".format(folder_name, folder_name))
    r4 = sudo("rm -rf {}/web_static".format(folder_name))
    r5 = sudo("rm -r  /data/web_static/current".format(folder_name))
    r6 = sudo("ln -s {} /data/web_static/current".format(folder_name))

    if r1.failed and r2.failed and r3.failed and r4.failed and r5.failed \
            and r6.failed:
        return False
    return True
