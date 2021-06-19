from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def get_data(symbol):
    #  krx = pd.read_html(requests.get(url, headers={'user-agent': 'Mozilla/5.0'}).text)[0]
    #req = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
    #        html = BeautifulSoup(req.text, "lxml")
    #        pgrr = html.find("td", class_="pgRR")
    url = r'https://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    req = requests.get(url, headers={'user-agent' : 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, 'lxml', from_encoding='euc-kr')
    cur_price = soup.find('strong', id='_nowVal') # id가 _nowVal인  스트롱 태그를 찾는다.
    cur_rate = soup.find('strong', id='_rate') # id가 _rate인 태그를 찾는다. 
    stock = soup.find('title')
    stock_name = stock.text.split(':')[0].strip() # title 태그에서 :(콜론) 문자를 기준으로 문자열을 분리하여 종목명을 구한뒤 문자열 좌우의 공백문자를 제거한다.
    return cur_price.text, cur_rate.text.strip(), stock_name

def main_view(request):
    querydict = request.GET.copy() # get 방식으로 넘어온 queryDict형태의 url을 리스트 형태로 변환한다.
    mylist = querydict.lists()
    rows = []
    total = 0

    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0]) # mylist의 종목 코드로 get_data함수를 호출하여 현재가 등락률, 종목명을 구한다.
        price = cur_price.replace(',','')
        stock_count = format(int(x[1][0]), ',') # mylist의 종목 수를 int형으로 변환한뒤 천단위 마다 쉼표를 포함하는 문자열로 변환한다.
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum]) # 종목명, 종목코드, 현재가, 주식수, 등락률, 평가 금액을 리스트로 생성해서 rows 리스트에 추가한다.
        total = total + int(price) * int(x[1][0]) # 평가 금액을 주식수로 곱한뒤 total변수에 더한다.

    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount} # balanc.html파일에 전달할 값들을 values딕셔너리에 저장한다.
    return render(request, 'balance.html', values) 

