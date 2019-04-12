import archiveis
import urllib
from os import system

URLS_FILE = './urls'
ZIPS_DIR = './export/tmp/'
SAVE_DIR = './export/wechat/'
FOOS_FILE = './foos'


def import_urls(filename):
    with open(filename) as file:
        content = file.readlines()
        content = [x.strip() for x in content]
    return content


def get_foo(url):
    archive_url = archiveis.capture(url)
    foo = archive_url.split('/')[-1]
    return foo


if __name__ == "__main__":
    URLS = import_urls(URLS_FILE)
    foo_list = []
    for url in URLS:
        foo = get_foo(url)
        print(foo)
        foo_list.append(foo)
    print(foo_list)

    f = open(FOOS_FILE, 'a')
    for foo in foo_list:
        f.write(foo + '\n')
    f.close()
