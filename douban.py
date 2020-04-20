#-*- coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import re
import xlwt
import xlrd
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#获取到源代码
# sclass = []
# ssclase = []
# daoyin = []
# rm = []
# quote =[]
def get_url_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    #try:
    r = requests.get(url,headers=headers)
    r.raise_for_status
    #print r.status_code
    return r.text
    #except:
        #print('fail')
#获取到豆瓣信息
def get_moice_html(lst,html):

    soup = BeautifulSoup(html,'html.parser')
    for di_tag in soup.find_all('ol',attrs={'class':'grid_view'}):
        #rank = di_tag.find('em').string
        #try:
        for di_info in di_tag.find_all('div',attrs={'class':'info'}):
            try:
                sclass = di_info.find('span',attrs={'class':'title'}).text #获取中文名称
                #ssclass = di_info.find('div',attrs={'class':'hd'}).a.contents[2] 
                ssclass = di_info.div.a.contents[3].text.strip()#获取英文名
                ssclass = ssclass[2:]
                # for name in ssclass:
                #     if name.find('/')==-1:
                #         return name

                pclass = di_info.find('div',attrs={'class':'bd'}).p.text.strip() #获取导演名
                xpclass = pclass.split(' ')[0]
                f = pclass.split(' ')[1]
                daoyin = xpclass+f
                #xpclass = pclass.split(' ')[0]
                
                rm = di_info.find('span',attrs={'class':'rating_num'}).text #电影评分
                #quote = ''
            # quote = di_info.xpath('div[@class="bd"]/p[2]/span/text()')

                quote = di_info.find('span',attrs={'class':'inq'}).text  #代表评论
            except:
                print('pass')
            
            # if quote != None:
            #     return quote
            # else:
            #     return None
            #print sclass,ssclass,daoyin,rm,quote
            # count = 0
            for count in range(0,250,1):
                count = count + 1
            lst.append([count,sclass,ssclass,daoyin,rm,quote])
        #except:
            #print('fail')
                
# def print_douban_m(lst):
#     path = 'D:/pythonpc/douban/dianyin.txt'
#     tplt = '{0:^1}\t{1:^13}\t{2:^60}\t{3:^30}\t{4:^3}\t{5:^20}\n'
#     with open(path,'a') as f:
#         f.write('') #清空原文件内容
#         #f.close()
#         f.write(tplt.format('N.O','name','enname','daoyin','score','title',unichr(12288)))
#     count = 0
#     #f = open(path,'w')
#     for i in lst:
#         count = count + 1
#         with open(path,'a') as f:
            
#             f.write(tplt.format(count,i[0],i[1],i[2],i[3],i[4],unichr(12288))+'\n')  
#             f.close()
def print_douban_m(lst): 
    #写入到excel里面

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('豆瓣电影Top250')
    into = ['N.O','name','enname','daoyin','score','title']
    
    for i in range(len(into)):
        sheet.write(0,i,into[i]) #0表示行 i表示列 into[i]表示
    j = 1 #定义行数，从1开始
    for l in lst:
        k = 0#定义列数从0开始
        for data in l:
            sheet.write(j,k,data)
            k = k+1
        j = j+1
    # excel_path = 'D:/pythonpc/douban/diany.xls'
    # data =xlrd.open_workbook(excel_path)
    # writh_data = copy(data)
    # writh_data.get_sheet(0).write(0,0,'排名')
    book.save('D:/pythonpc/douban/diany.xls')

def main():
    alist = []
    for num in range(0,250,25):
        url = 'https://movie.douban.com/top250?start='+str(num)
        html = get_url_html(url)
        get_moice_html(alist,html)
        print_douban_m(alist)

if __name__ == "__main__":
    main()



    