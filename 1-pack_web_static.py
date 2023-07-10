#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions
(your function should create this folder if it doesn't exist)
The name of the archive created must be,
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has
been correctly generated. Otherwise, it should return None
"""


from fabric.api import local
from time import strftime


def do_pack():
    """Generate archive(.tgz) of web_static folder"""
    current_time = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception as e:
        return None
