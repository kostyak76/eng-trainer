from csv import DictWriter


def main():
    with open('../data/words.txt', 'r') as words_source:
        words_iter = iter(words_source)
        with open('../data/translation.txt', 'r') as translation_source:
            tr_iter = iter(translation_source)
            with open('../data/dictionary.csv', 'w') as destination:
                field_names = ['word', 'translation']
                writer = DictWriter(destination, fieldnames=field_names)

                writer.writeheader()
                for word in words_iter:
                    writer.writerow({'word': word.strip("\n"), 'translation': next(tr_iter).strip("\n")})


if __name__ == '__main__':
    main()
