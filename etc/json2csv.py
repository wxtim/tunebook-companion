"""Convert this applications "database" (the json file) to a CSV

to use

python etc/json2csv.py
"""

import json
from pathlib import Path


PATH = Path(__file__).parent.parent / 'src/components/tunebooks.json'
OUT_PATH = Path(__file__).parent / 'tunebooks.csv'


data = json.loads(PATH.read_text())['bookData']
linerized_data = []
for book, editions in data.items():
    for edition, tunes in editions.items():
        for tune, page in tunes.items():
            linerized_data.append([book, edition, tune, page])

OUT_PATH.write_text('\n'.join(['|'.join(i) for i in linerized_data]))

