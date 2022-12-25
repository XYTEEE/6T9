import os, platform
from os import path,system
from platform import uname
arch=uname().machine.lower()
os.system('git pull')
if 'aarch' in arch:
	os.system('python .sex.so')
else:
	os.system('python .sex.so')
