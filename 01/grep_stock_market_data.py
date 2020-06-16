import sys
import requests

sina_stock_api = 'http://hq.sinajs.cn/'

if len(sys.argv) > 1:
    stocks = sys.argv[1]  # argv[0] is your python prog name
else:
    stocks = 'sh000001,sz399001'

response = requests.get(f'{sina_stock_api}/list={stocks}').text

for line in response.splitlines():
    stock_id = line[11:19]
    stock_data = line[21:-1].split(',')

    print(f'{stock_data[0]} - 数据如下：')
    print('{0:->10}: {1:<10}'.format('股票代码', stock_id))
    print('{0:->10}: {1:<10}'.format('股票名称', stock_data[0]))
    print('{0:->10}: {1:<10}'.format('今日开盘', stock_data[1]))
    print('{0:->10}: {1:<10}'.format('昨日收盘', stock_data[2]))
    print('{0:->10}: {1:<10}'.format('当前', stock_data[3]))
    print('{0:->10}: {1:<10}'.format('今日最高', stock_data[4]))
    print('{0:->10}: {1:<10}'.format('今日最低', stock_data[5]))




