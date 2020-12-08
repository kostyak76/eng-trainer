from csv import DictWriter

from bs4 import BeautifulSoup


def get_table_rows(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find_all('tr')


def get_word(row):
    tabs = row.find_all('td')
    try:
        assert len(tabs) == 4
    except AssertionError:
        print(f"Could not read from: {row}")

    return tabs[1].text


def clean_word(raw_word):
    return raw_word.strip('\t\n')


def is_big(word):
    return len(word) > 3


def main():
    with open('../data/source.html', 'r') as data_file:
        content = data_file.read()

    table_rows = get_table_rows(content)
    raw_words = map(get_word, table_rows[1:])
    clean_words = map(clean_word, raw_words)
    big_words = filter(is_big, clean_words)
    # with open('../data/words.csv', 'w') as words_file:
    #     field_names = ['word']
    #     writer = DictWriter(words_file, fieldnames=field_names)
    #
    #     writer.writeheader()
    #     for word in big_words:
    #         writer.writerow({'word': word})
    lines = map(lambda w: f"{w}\n", big_words)
    with open('../data/words.txt', 'w') as words_file:
        words_file.writelines(lines)


if __name__ == '__main__':
    main()
