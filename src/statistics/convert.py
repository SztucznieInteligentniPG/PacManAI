from __future__ import annotations
import json


if __name__ == '__main__':
    fileName = '2021-06-01_21_00_45'

    file = open(fileName, 'r')
    data = json.load(file)

    data = list(map(lambda x: {'seed': None, 'population': x}, data))

    with open(fileName + '_conv', 'w') as outfile:
        json.dump(data, outfile)
