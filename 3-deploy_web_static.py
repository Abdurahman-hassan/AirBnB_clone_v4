#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""
from importlib import import_module

from fabric.api import env

do_deploy_module = import_module('2-do_deploy_web_static')
do_pack_module = import_module('1-pack_web_static')

do_deploy = do_deploy_module.do_deploy
do_pack = do_pack_module.do_pack

env.hosts = ['18.206.207.101', '54.174.244.164']
env.user = 'ubuntu'


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
