#!/usr/bin/env bash
"""Deploy new archive releases
to web servers
"""
import os
from fabric.api import run, env, put, sudo


env.hosts = ["54.234.93.141", "34.207.154.98"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Deploy new archive releases
        to web servers
    """
    archive_name = os.path.basename(archive_path).split(".")[0]
    if not os.path.exists(archive_path):
        return False
    temp_archive, = put(local_path=archive_path, remote_path="/tmp")
    folder_name = "/data/web_static/releases/{}".format(archive_name)
    sudo("mkdir -p {}".format(folder_name))
    sudo("tar -xzvf {} -C {}".format(temp_archive, folder_name))
    sudo("mv {}/web_static/* {}".format(folder_name, folder_name))
    sudo("rm -rf {}/web_static".format(folder_name))
    sudo("rm -r  /data/web_static/current".format(folder_name))
    sudo("ln -s {} /data/web_static/current".format(folder_name))
