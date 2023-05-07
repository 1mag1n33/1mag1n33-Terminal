import requests
import zipfile
import os
import shutil
import json
import time
from src.imports import settings
from github import Github
# create a Github instance

def update():
    g = Github()

    with open(settings, 'r') as f:
                server_config = json.load(f)

    version = server_config.get('version')
            # get the repository by name and owner
    repo = g.get_repo("1mag1n33/1mag1n33-Terminal")

            # get the latest release tag with prefix "v"
    latest_tag = None
    for tag in repo.get_tags():
                if tag.name.startswith("v"):
                    commit = tag.commit
                    if not latest_tag or commit.committer.created_at > latest_tag.commit.committer.created_at:
                        latest_tag = tag

    if not latest_tag:
                print("Latest tag not found")
    else:
        print(f"Latest tag found: {latest_tag.name}")
        # get the latest release associated with the tag
        latest_release = None
        for release in repo.get_releases():
            if release.tag_name == latest_tag.name:
                latest_release = release
                break

            if not latest_release:
                print("Latest release not found")
            elif latest_tag.name == version:
                print("Already up-to-date")
            else:
                # download the latest release asset
                download_url = latest_release.zipball_url
                r = requests.get(download_url)
                with open("new_files.zip", "wb") as f:
                    f.write(r.content)

                print("Downloaded the latest release asset")

                    # extract the contents of the zip file
                with zipfile.ZipFile("new_files.zip", "r") as zip_ref:
                    zip_ref.extractall("new_files")

                print("Extracted the contents of the zip file")

                    # delete the zip file
                os.remove("new_files.zip")

                print("Deleted the zip file")

                    # replace old files with new ones
                if os.path.exists("old_files"):
                    shutil.rmtree("old_files")
                shutil.move("new_files", "old_files")
                    


                print("Replaced old files with new ones")

                    # update the version in the config file

                server_config['version'] = latest_tag.name
                with open(settings, 'w') as f:
                    json.dump(server_config, f, indent=4, sort_keys=True)

                print("Updated the version in the config file")

                print("Downloaded and installed the latest version")

                time.sleep(1)