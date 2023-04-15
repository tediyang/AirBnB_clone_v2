#!/usr/bin/python3
"""
    Fabfile to deploy to remote server
"""

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """function automatically convert to archive and deploy"""

    from fabfile.api import env

    env.user = "ubuntu"
    env.hosts = ["52.72.26.101", "100.25.162.157"]
    env.key_filename = '~/.ssh/id_rsa'

    archive = do_pack()
    if not archive:
        return False

    return do_deploy(archive)
