import pytest
from pageObjects.google import googleResult
from pageObjects.yahoo import yahooResult
from pageObjects.bing import bingResult
from testCases.collection import get_data
import csv
from pathlib import Path


datafile = 'data.csv'
cfgFileDirectory = 'file'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)


insert = []

@pytest.mark.parametrize("data", get_data())
def test_run(data):
    insert.append([data, googleResult(data), yahooResult(data), bingResult(data)])

    with open(BASE_DIR.joinpath(cfgFileDirectory).joinpath('search_output.csv'), 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['search text', 'Google result', 'yahoo result', 'Bing result'])
        spamwriter.writerows(insert)
        csvfile.close()

# test_run(get_data())