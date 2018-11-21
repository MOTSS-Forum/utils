import archiveis
import urllib
from os import system

URLS_FILE = './urls'
ZIPS_DIR = './export/tmp/'
SAVE_DIR = './export/wechat/'
FOOS_FILE = './foos'

def download_zip(foo: str):
    cmd = "curl 'https://archive.today/download/{}.zip' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36' --output {}{}.zip".format(
        foo, ZIPS_DIR, foo)
    system(cmd)

def unzip(foo: str):
    cmd = "mkdir -p {}{}".format(SAVE_DIR, foo)
    system(cmd)
    cmd = "unzip {}{}.zip -d {}{}".format(ZIPS_DIR, foo, SAVE_DIR, foo)
    system(cmd)

if __name__ == "__main__":
    with open(FOOS_FILE) as file:
        foo_list = file.readlines()
        foo_list = [x.strip() for x in foo_list]
    for foo in foo_list:
        print(foo)
        download_zip(foo)
        unzip(foo)
