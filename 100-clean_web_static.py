#!/usr/bin/python3
"""
    Script that Clean up the archive files on the server
"""
from fabric.api import run, env, local
import os

env.user = "ubuntu"
env.hosts = ["52.72.26.101", "100.25.162.157"]
env.path_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """ clean archive files on the server """

    if os.path.exists("versions/"):
        if number == 0 or number == 1:
            local("ls -1tr versions/*.tgz | head -n -1 | xargs rm -rf")
        else:
            local(f"ls -1tr versions/*.tgz | head -n -{number} | xargs rm -rf")

    path = "/data/web_static/releases/*/"
    try:
        if number == 0 or number == 1:
            run(f"sudo ls -1tr {path} | head -n -1 | xargs rm -rf")
        else:
            run(f"sudo ls -1tr {path} | head -n -{number} | xargs rm -rf")
        return True

    except Exception as e:
        return False
