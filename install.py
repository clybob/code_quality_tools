import platform
import os


def main():
    is_mac = len(platform.mac_ver()[0])
    is_linux = len(platform.linux_distribution()[0])
    make_path = os.path.abspath(os.path.join(os.path.dirname('')))

    if is_mac:
        os.system("make -C %s install_mac" % make_path)
    elif is_linux:
        os.system("make -C %s install_linux" % make_path)

main()
