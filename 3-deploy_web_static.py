#!/usr/bin/python3
"""Automate deployment of static
content from the packaging of files to
deployment on the server
"""
from datetime import datetime
from fabric.api import local, run, env, put, runs_once
import os


env.hosts = ["54.234.93.141", "34.207.154.98"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


@runs_once
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
    r1 = run("mkdir -p {}".format(folder_name))
    r2 = run("tar -xzf {} -C {}".format(temp_archive, folder_name))
    r6 = run("rm {}".format(temp_archive))
    r3 = run("mv {}/web_static/* {}".format(folder_name, folder_name))
    r4 = run("rm -rf {}/web_static".format(folder_name))
    r5 = run("rm -r  /data/web_static/current".format(folder_name))
    r7 = run("ln -s {} /data/web_static/current".format(folder_name))

    if r1.failed and r2.failed and r3.failed and r4.failed and r5.failed \
            and r6.failed and r7.failed:
        return False
    return True


def deploy():
    """Deploys the web static content on the
    web-1 and web-2 servers automatically
    """
    packed_path = do_pack()
    if packed_path is None:
        return False

    return do_deploy(packed_path)
