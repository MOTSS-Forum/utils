from os import walk
from yaml import load, dump

BASE_DIR = './export/wechat/'
SAVES = './export/saves.yml'
README = './export/README.md'


def generate_yml(pages):
    pages_list = []
    for item in pages:
        pages_list.append({
            'title': item[0],
            'url': item[1]
        })
    content = {
        'pages': pages_list,
        'description': '',
        'title': '微信公众号存档',
    }
    with open(SAVES, 'w') as file:
        dump(content, file, allow_unicode=True)
    return


def generate_readme():
    with open(SAVES, 'r') as file:
        content = load(file)

    content_str = '## {}\n\n'.format(content['title'])
    for page in content['pages']:
        content_str += '- [{}]({})\n'.format(page['title'], page['url'])

    with open(README, 'w') as file:
        file.write(content_str)

    return


def parse_page(foo):
    index_file = BASE_DIR + foo + '/index.html'
    with open(index_file) as file:
        content = file.readlines()
        content = [x.strip() for x in content]
    title = content[95][:-6].replace("|", "/")
    # date = content[121][-10:-5]
    url = './{}/'.format(foo)
    return title, url


def load_foos(BASE_DIR):
    foos = []
    for _, dirs, _ in walk(BASE_DIR):
        for filename in dirs:
            foos.append(filename)
    return foos


if __name__ == "__main__":
    foos = load_foos(BASE_DIR)
    pages = []
    for foo in foos:
        pages.append(parse_page(foo))
    generate_yml(pages)
    generate_readme()
