import httpx
import json 
import sqlite3

URLS = [
    ('可售', 'http://zfcj.gz.gov.cn/zfcj/tjxx/mrxjspfksxxRequest'),
    ('未售', 'http://zfcj.gz.gov.cn/zfcj/tjxx/mrxjspfwsxxRequest'),
    ('签约', 'http://zfcj.gz.gov.cn/zfcj/tjxx/mrxjspfqyxxRequest'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Languag': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'}

def request_data(url):
    response = httpx.post(url, headers=headers)
    return json.loads(response.json()).get('data')

def save_data(data):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.executemany('INSERT INTO gzdata VALUES (?,?,?,?,?,?,?,?,?,?,?)', data)
    con.commit()
    con.close()
    
def data_init():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    sql_init = """
    CREATE TABLE IF NOT EXISTS gzdata(
        type text,
        create_time text,
        area text,
        house_num int,
        house_area float,
        commercial_units_num int,
        commercial_units_area float,
        office_units_num int,
        office_units_area float,
        park_num int,
        park_area float
    )
    """
    cur.execute(sql_init)
    con.commit()
    con.close()

def main():
    data_init()
    for type, url in URLS:
        data = request_data(url)
        data = [(type, *(d.values())) for d in data]
        save_data(data)

if __name__ == '__main__':
    main()