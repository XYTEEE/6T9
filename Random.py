import os, platform
from os import path,system
from platform import uname
arch=uname().machine.lower()
os.system('git pull')
if 'aarch' in arch:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    if path.isfile("XD.so"):
        pass
    else:
        system("curl -L https://github.com/XYTEEE/RANDOM/blob/main/sex.so")
        os.system('xdg-open https://www.facebook.com/ps7c8o.p133h1')
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
import sex
sex.main()
