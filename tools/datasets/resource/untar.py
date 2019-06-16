import math
import os
import random
import tarfile
import glob

def _get_members(filename):
    """Get all members of a tarfile."""
    tar = tarfile.open(filename)
    members = tar.getmembers()
    tar.close()
    return members

def _untar_file(filename, directory, member=None):
    """Untar a file at the provided directory path."""
    tar = tarfile.open(filename)
    if member is None:
      tar.extractall(path=directory)
    else:
      tar.extract(member, path=directory)
    tar.close()

directory = os.path.join('./')
tarfiles = glob.glob(os.path.join('*.tar'))
#print(directory)
#print(tarfiles)

for filename in tarfiles:
    subdirectory = os.path.join(directory, filename.split('.')[0])
    sub_tarfile = os.path.join(directory, filename)
    print(subdirectory)
    print(sub_tarfile)
    _untar_file(sub_tarfile, subdirectory)
    #os.remove(sub_tarfile)

