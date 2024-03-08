#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo"""

import os
from datetime import datetime

from fabric.api import local


def do_pack():
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate a timestamped archive name
        now = datetime.now()  # Current date and time
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # The folder to archive
        folder_to_archive = "web_static"

        # The target archive path
        archive_path = "versions/{}".format(archive_name)

        # Create the archive using tar command
        command = "tar -cvzf {} {}".format(archive_path, folder_to_archive)
        print("Packing {} to {}".format(folder_to_archive, archive_path))

        # Execute the command locally
        local(command)

        return archive_path
    except:
        return None

