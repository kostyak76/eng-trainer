import requests


def main():
    page = requests.get('https://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx')
    content = page.text
    with open('../data/source.html', 'w') as data_file:
        data_file.write(content)


if __name__ == '__main__':
    main()
