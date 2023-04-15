#!/usr/bin/python3
""" Fabfile to deploy to remote server """

from fabfile.api import env
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.user = "ubuntu"
env.hosts = ["52.72.26.101", "100.25.162.157"]
env.key_filename = '~/.ssh/id_rsa'

def deploy():
    """automatically convert to archive and deploy"""

    archive = do_pack()
    if not archive:
        return False

    return do_deploy(archive)
