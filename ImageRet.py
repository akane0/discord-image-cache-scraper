import os
import shutil
import errno
from datetime import date

def CreateDirectories(): # eventually add specific folders for dates

    today = date.today().isoformat()
    path = os.getcwd()
    image_dir = path + "\\images\\" + today
    temp_dir = path + "\\temp"

    directories = [image_dir, temp_dir]

    print("Detected root directory: %s \n" % path)

    for x in directories:
        if not os.path.exists(x):
            print("Creating image directory: %s" % x)
            try:
                os.makedirs(x)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        else:
            print("Found %s directory.." % x)
    return image_dir, temp_dir


def FindDiscordDirectory():
    print(r"Checking for default Discord cache directory (C:\Users\USER\AppData\Roaming\discord\Cache)..")

    discord_path = os.getenv('APPDATA') + r"\discord\Cache"

    if os.path.exists(discord_path):
        print("Found directory: %s" % discord_path)
    else:
        print("Could not find Discord cache...\n")
        discord_path = input("Manually input discord cache path: ")
        print("Set directory to: %s" % discord_path)
    return discord_path


def CopyFiles(discord_path, temp_dir, image_dir):
    print("Preparing to copy files over..")

    print(discord_path, temp_dir, image_dir)

    file_blacklist = os.listdir(image_dir)
    files = os.listdir(discord_path)

    for file in files:
        if file in file_blacklist:
            continue
        else:

            src = r"{}\{}".format(discord_path, file)

            shutil.copy(src, temp_dir)

            print("Copying %s over..." % file)
    print("Finished copying over files.")


def ConvertFiles(temp_dir, image_dir):

    print("Coverting files to .png files...")

    files = os.listdir(temp_dir)

    for file in files:
        src = temp_dir + "\\" + file
        dest = image_dir + "\\" + file + ".png"

        print("Coverting file %s" % file)

        shutil.move(src, dest)


def main():

    image_dir, temp_dir = CreateDirectories()
    print("Image Directory: {}\nTEMP Directory: {}\n".format(image_dir, temp_dir))

    discord_path = FindDiscordDirectory()
    print("Discord Path: {}\n".format(discord_path))

    CopyFiles(discord_path, temp_dir, image_dir)

    ConvertFiles(temp_dir, image_dir)

    print("Finished transfer and conversion.")


if __name__ == "__main__":
    main()
