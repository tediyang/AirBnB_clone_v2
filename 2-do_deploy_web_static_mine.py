#!/usr/bin/python3
"""A script to send an archive file to a remote server
decompress it and setup the file on the server."""

from fabric.api import run, env, put
import os

env.user = "ubuntu"
env.hosts = ["52.72.26.101", "100.25.162.157"]
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """A script that distributes an archive to the web servers."""

    if not os.path.isfile(archive_path):
        return False

    archive = archive_path.split("/")[-1]
    no_extension = archive.split(".")[0]

    """ 
    # copy the file from local to remote.
    # create directory if not available.
    # decompress file
    # remove archive
    # move file from directory and delete directory
    # remove symbolic link
    # create a new symlink with current web static """
    try:
        sym_link = "/data/web_static/current"
        path = f"/data/web_static/releases/{no_extension}/"
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {path}")
        run(f"sudo tar -xvf /tmp/{archive} -C {path}")
        run(f"sudo rm /tmp/{archive}")
        run(f"sudo mv {path}/web_static/* {path}")
        run(f"sudo rmdir {path}/web_static")
        run(f"sudo rm -rf {sym_link}")
        run(f"sudo ln -s -f /data/web_static/releases/web* {sym_link}")
        return True

    except Exception as e:
        return False
