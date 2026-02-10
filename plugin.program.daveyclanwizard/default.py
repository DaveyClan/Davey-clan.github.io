import xbmc
import xbmcgui
import xbmcvfs
import zipfile
import os
import urllib.request
import shutil

ADDON_NAME = "Davey Clan Wizard"

BUILD_URL = "https://github.com/USERNAME/REPO/raw/main/DaveyBuild.zip"

TEMP_ZIP = "special://home/temp/daveyclan_build.zip"
KODI_HOME = "special://home/"

def notify(title, message):
    xbmcgui.Dialog().notification(title, message, xbmcgui.NOTIFICATION_INFO, 3000)

def main():
    dialog = xbmcgui.Dialog()

    choice = dialog.yesno(
        plugin.program.daveyclanwizard,
        "This will install the Davey Clan build.",
        "Your current Kodi setup will be replaced.",
        "",
        "Cancel",
        "Install"
    )

    if not choice:
        return

    notify(plugin.program.daveyclanwizard, "Downloading build...")

    zip_path = xbmcvfs.translatePath(TEMP_ZIP)
    kodi_path = xbmcvfs.translatePath(KODI_HOME)

    os.makedirs(os.path.dirname(zip_path), exist_ok=True)

    try:
        urllib.request.urlretrieve(BUILD_URL, zip_path)
    except Exception as e:
        dialog.ok(plugin.program.daveyclanwizard, "Download failed", str(e))
        return

    notify(plugin.program.daveyclanwizard, "Extracting build...")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(kodi_path)
    except Exception as e:
        dialog.ok(plugin.program.daveyclanwizard, "Extraction failed", str(e))
        return

    try:
        os.remove(zip_path)
    except:
        pass

    dialog.ok(
        plugin.program.daveyclanwizard,
        "Build installed successfully.",
        "Kodi will now close."
    )

    xbmc.executebuiltin("Quit")

if __name__ == "__main__":
    main()