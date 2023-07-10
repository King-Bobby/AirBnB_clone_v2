#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""


from fabric.api import env, run, put
import os.path
env.hosts = ['3.90.65.16', '52.91.150.159']


def do_deploy(archive_path):
    """Distribute archive to webservers"""
    if os.path.isfile(archive_path) is False:
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/' + archive_filename[:-4]
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf {}/web_static'.format(release_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_folder))
        return True
    except Exception as e:
        return False
