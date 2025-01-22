import json
from pathlib import Path

PATH = Path(__file__).parent.parent / 'src/components/tunebooks.json'
OUT_PATH = Path(__file__).parent / 'tunebooks.csv'


def main():
    data = json.loads(PATH.read_text())['bookData']
    linerized_data = []
    for book, editions in data.items():
        for edition, tunes in editions.items():
            for tune, page in tunes.items():
                linerized_data.append([book, edition, tune, page])

    with open('../tunebooks.csv', 'w') as fh:
        fh.write('\n'.join(['|'.join(i) for i in linerized_data]))

if __name__ == '__main__':
    main()
