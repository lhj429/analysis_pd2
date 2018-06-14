import os
import json
from .api import  api

RESULT_DIRECTORY = '__results__/crawling'

def preprocess_post(data):
    rm = ['ed', 'edCd', 'rnum', 'natCd', 'natKorNm', 'num', 'ym']

    data['country_code'] = data['natCd']
    data['country_name'] = data['natKorNm'].replace(' ', '')
    data['visit_count'] = data['num']
    data['date'] = data['ym']

    for delete in rm:
        if delete in data:
            del data[delete]

def crawlling_foreign_visitor(country, start_year, end_year):
    results = []
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country[0], country[1], start_year, end_year)

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            data = api.pd_fetch_foreign_visitor(country[1], year, month)
            if data is None:
                continue

            preprocess_post(data)
            results.append(data)

    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)