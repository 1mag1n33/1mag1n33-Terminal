class Update():
    import requests
    import json

    manifest_url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'

    # Retrieve manifest JSON data
    manifest_data = requests.get(manifest_url).json()

    # Get latest version's download URL
    latest_version = manifest_data['latest']['release']
    latest_version_url = None
    for version in manifest_data['versions']:
        if version['id'] == latest_version:
            latest_version_url = version['url']
            break

    if latest_version_url is None:
        print('Latest version URL not found in manifest.')
    else:
        # Retrieve latest version JSON data
        version_data = requests.get(latest_version_url).json()

        # Get latest version's .jar file download URL
        jar_url = version_data['downloads']['server']['url']
        # Download .jar file
        jar_filename = jar_url.split('/')[-1]
        with open(jar_filename, 'wb') as f:
            jar_data = requests.get(jar_url)
            f.write(jar_data.content)
