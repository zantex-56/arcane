import os
import pwd
import stat
import sys

def create_ct_base(system, name, path=None):
    """
    Create a new CT instance.
    """
    if path is None:
        path = name
    if system == "noble":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase noble {path} http://archive.ubuntu.com/ubuntu")
    elif system == "bookworm":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase bookworm {path} http://deb.debian.org/debian")
    elif system == "jammy":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase jammy {path} http://archive.ubuntu.com/ubuntu")
    elif system == "focal":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase focal {path} http://archive.ubuntu.com/ubuntu")
    elif system == "buster":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase buster {path} http://deb.debian.org/debian")
    elif system == "bullseye":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase bullseye {path} http://deb.debian.org/debian")
    elif system == "sid":
        os.system(f"sudo debootstrap --arch=amd64 --variant=minbase sid {path} http://deb.debian.org/debian")
    else:
        raise ValueError("Unsupported OS. Supported OS are: noble, bookworm, jammy, focal, buster, bullseye, sid")
    print("Starting Container")
    os.system(f"sudo chroot {path} /bin/bash")
    
def access_ct(path):
    """
    Access a CT instance.
    """
    if not os.path.exists(path):
        raise ValueError(f"CT instance {path} does not exist.")
    os.system(f"sudo chroot {path} /bin/bash")