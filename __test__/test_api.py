import analysis_pd2.collect.api.api as pdapi
'''
url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
    YM = '{0:04d}{1:02d}'.format(2012, 7),
    NAT_CD = 112,
    ED_CD = 'E',
    _type = 'json')
print(url)
'''

# test for pd_fetch_foreign_visitor
item = pdapi.pd_fetch_foreign_visitor(112, 2012, 7)
print(item)
