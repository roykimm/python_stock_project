import pandas as pd
from bs4 import BeautifulSoup
import urllib, pymysql, calendar, time, json
from urllib.request import urlopen
from datetime import datetime
from threading import Timer
import requests


def update_stock_code():
    conn = pymysql.connect(host='18.222.188.155', user='root',
            password='Tftfat024!!', db='investar', charset='utf8')
        
    with conn.cursor() as curs:
        sql = """
        CREATE TABLE IF NOT EXISTS company_info (
            code VARCHAR(20),
            company VARCHAR(40),
            last_update DATE,
            PRIMARY KEY (code))
        """
        curs.execute(sql)
        sql = """
        CREATE TABLE IF NOT EXISTS daily_price (
            code VARCHAR(20),
            date DATE,
            open BIGINT(20),
            high BIGINT(20),
            low BIGINT(20),
            close BIGINT(20),
            diff BIGINT(20),
            volume BIGINT(20),
            PRIMARY KEY (code, date))
        """
        curs.execute(sql)
    conn.commit()

    company_code = '035420'
    company_name = 'NAVER'
    print('업데이트 시작')
    try:
        url = f"http://finance.naver.com/item/sise_day.nhn?code={company_code}"
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
        html = BeautifulSoup(req.text, "lxml")
        pgrr = html.find("td", class_="pgRR")
        if pgrr is None:
            return None
        s = str(pgrr.a["href"]).split('=')
        lastpage = s[-1] 
        print("lastpage : " + str(lastpage))
        df = pd.DataFrame()
        #pages = min(int(lastpage), pages_to_fetch)
        pages = min(int(lastpage),1) 
        print("pages : " + str(pages))
        for page in range(1, pages + 1):
            pg_url = '{}&page={}'.format(url, page)
            df = df.append(pd.read_html(requests.get(pg_url, headers={'user-agent': 'Mozilla/5.0'}).text)[0])
            tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
            print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.
                format(tmnow, company_name, company_code, page, pages), end="\r")
        df = df.rename(columns={'날짜':'date','종가':'close','전일비':'diff'
            ,'시가':'open','고가':'high','저가':'low','거래량':'volume'})
        df['date'] = df['date'].replace('.', '-')
        df = df.dropna()
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
            'diff', 'open', 'high', 'low', 'volume']].astype(int)
        df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
    except Exception as e:
        print('Exception occured :', str(e))
        return '실패'
    return '완료'
