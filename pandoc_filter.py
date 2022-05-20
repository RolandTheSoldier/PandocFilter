from panflute import *
import sys

all_headers = {}


def action(phrase, doc):
    if type(phrase) == Header:
        if stringify(phrase) in all_headers.keys():
            if all_headers.get(stringify(phrase)) == phrase.level:
                sys.stderr.write("Repeated headers. Level: " + str(phrase.level) + ", text: " + stringify(phrase))
        else:
            all_headers[stringify(phrase)] = phrase.level

    if type(phrase) == Header:
        if phrase.level <= 3:
            title = [Str(stringify(phrase).upper())]
            return Header(*title, level=phrase.level)

    if type(phrase) == Str:
        if str(phrase.text).lower() == "bold":
            title = [Str(phrase.text)]
            return Strong(*title)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
