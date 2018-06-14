from urllib.parse import urlencode
from .web_request import json_request
from datetime import *

SERVICE_KEY = 'kglFus9rQiSwGqFYcuHmr87yibNi7qlvrcMbHW1JBvzsbgfwovIZpBJsQ0tDK0osX9ySfBxiPrqY%2BrnoEoYvKQ%3D%3D'
END_POINT = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

def pd_gen_url(endpoint, **params):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), SERVICE_KEY)
    return url

def pd_fetch_foreign_visitor(country_code, year, month):
    url = pd_gen_url(END_POINT,
                     YM = '{0:04d}{1:02d}'.format(year, month),
                     NAT_CD = country_code,
                     ED_CD = 'E',
                     _type = 'json')

    json_result = json_request(url=url)
    json_header = json_result.get('response').get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_result.get('response').get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None
