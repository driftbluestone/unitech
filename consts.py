import json
from pathlib import Path
DIR = Path(__file__).absolute().parent
phi = (((5 ** 0.5) + 1) / (2*3.1415926535897932384626))

with open(f"{DIR}/star_data.json", "r") as file:
    star_data = json.load(file)