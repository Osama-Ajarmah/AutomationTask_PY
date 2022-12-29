import csv
from pathlib import Path

datafile = 'data.csv'
cfgFileDirectory = 'file'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)

def get_data():
     with open(DATA_FILE, 'r') as f:
         reader = csv.reader(f)
         next(reader) #skipping the first row
         data = [row[0] for row in reader ]

     return data

print(get_data())