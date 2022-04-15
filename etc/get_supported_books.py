"""List supported books for use in Readme

Consider making this a catch all json-csv util
"""

import json
from pathlib import Path


def load_bookdata(jsonpath):
    with open(jsonpath, 'r') as fh:

        data = json.load(fh)
    return data


def format_bookdata(data):
    return ''.join([
        '#### ' + book + '\n' + ''.join(
            ["  - " + e + "\n" for e in edition.keys()]
        ) 
        for book, edition 
        in data['bookData'].items()
    ])



def main():
    jsonpath = Path(__file__).parent / '../src/components/tunebooks.json'
    data = load_bookdata(jsonpath)
    print(format_bookdata(data))


if __name__ == '__main__':
    main()
