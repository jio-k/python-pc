# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import xlwt
import re
from scrapy import Selector
from pcsql.doubandb import doubanbook
#from urllib import parse
#from pc.pcsql.doubandb import doubanbook
def get_url_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status
        return r.text
    except:
        print('request url fail')

def parser_book(html):
    sel = Selector(text=html)
    divitem = sel.xpath('.//tr[@class="item"]')
    for dit in divitem:
        try:
            dbook = doubanbook()    
            bname = dit.xpath('.//div[@class="pl2"]/a/@title').extract()[0]
            dbook.name = bname
            author_info = dit.xpath('.//p[@class="pl"]/text()').extract()[0]
            author_name = author_info.split('/')[0]
            dbook.zuozhe = author_name
            author_cbs = author_info.split('/')[-3]
            dbook.chubanshe=author_cbs
            author_price = author_info.split('/')[-1]
            dbook.price = author_price
            score = dit.xpath('.//span[@class="rating_nums"]/text()').extract()[0]
            dbook.pingfen = score
            pingjia_info = dit.xpath('.//span[@class="pl"]/text()').extract()[0].strip()
            book_pj = ''.join(pingjia_info.split())
            dbook.pingjia = book_pj
            #book_pjr = re.findall(r'(\w*[0-9]+)\w*',book_pj)
            inq = dit.xpath('.//span[@class="inq"]/text()').extract()[0]
            dbook.hope = inq
            
            dbook.save()
        except:
            pass

    # next_page = sel.xpath('//span[@class="next"]/a/@href').extract()
    # if next_page:
    #     page_url = next_page[0]
    #     get_url_html(page_url)
    #print book_pj
            



if __name__ == "__main__":
    for i in range(0,250,25):
        url = ('https://book.douban.com/top250?start={}'.format(i))
        html = get_url_html(url)
        parser_book(html)
#解析豆瓣数据
# def html_parser_book(lst,html):#定义一个字典用来存储数据
#     soup = BeautifulSoup(html,'html.parser')
#     for di_indet in soup.find_all('tr',attrs={'class':'item'}):
#         # quote = di_info.xpath('div[@class="bd"]/p[2]/span/text()
#         #name = di_indet.find('div',attrs={'class':'pl2'}).text.strip()
#         #name = di_indet.xpath('div/table[1]/tr/td[2]/div[1]/a/text()')[0].strip()
#         try:
#             book_name = di_indet.find('div',attrs={'class':'pl2'}).find('a')['title']#获取书名
#             name_all = di_indet.find('p',attrs={'class':'pl'}).text   #作者/出版社/出版时间/价格
#             book_author = name_all.split('/')[0] #作者名字
#             book_chu = name_all.split('/')[-3] #出版社名字
#             book_time = name_all.split('/')[-2] #出版时间
#             book_price = name_all.split('/')[-1] #价格
#             book_score = di_indet.find('span',attrs={'class':'rating_nums'}).text
#             book_pjrs = di_indet.find('span',attrs={'class':'pl'}).text #评价人数
#             book_pjrs = ''.join(book_pjrs.split())
#             #book_pjrs = ''.join(book_pjrs.split('()'))
#             book_inq = di_indet.find('span',attrs={'class':'inq'}).text

#             lst.append([book_name,book_author,book_chu,book_time,book_price,book_score,book_pjrs,book_inq])
#         except:
#             print ('fail')



# #定义一个输出函数
# def print_book_excel(lst,excel_path):
    
#     shouhang = ['No','bookname','bookauthor','bookchu','booktime','bookprice','bookscore','bookpjrs','inq']
#     data = xlwt.Workbook(encoding='utf-8')
#     sheet = data.add_sheet('豆瓣读书Top250')
#     for i in range(len(shouhang)):
#         sheet.write(0,i,shouhang[i])
#     #定义行数
#     j = 1
#     for lt in lst:
#         k = 0#定义列数
#         for h in lt:
#             sheet.write(j,k,h)
#             k = k+1

#         j = j+1
    
#     data.save(excel_path)


# def main():
#     lst =  []
#     excel_path = 'D:/pythonpc/douban/doubanbook.xls'
#     for num in range(0,250,25):
#         url = 'https://book.douban.com/top250?start='+str(num)
        
#         html = get_url_html(url)
#         html_parser_book(lst,html)
#         print_book_excel(lst,excel_path)
