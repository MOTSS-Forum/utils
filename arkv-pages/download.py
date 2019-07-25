import archiveis
import urllib
from os import system

URLS_FILE = './urls'
ZIPS_DIR = './export/tmp/'
SAVE_DIR = './export/wechat/'
FOOS_FILE = './foos'


def download_zip(foo: str):
    cmd = "curl 'https://archive.fo/download/{}.zip' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36' -H 'authority: archive.is' -H 'pragma: no-cache' -H 'cache-control: no-cache' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' -H 'cookie: _ga=GA1.2.661111166.1542719295;tmr_detect=1%7C1542719296018' --output {}{}.zip".format(
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
