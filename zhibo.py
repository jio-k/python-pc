#-*- coding:utf-8 -*-
import requests,re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class zhibo(object):
    def html_url(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        r = requests.get(url,headers=headers)
        r.raise_for_status
        return r.text

    #分析获取到的网页
    def html_parser(self,htmls):
        root_pattern = r'<li class="game-live-item" gid="1">([\s\S]*?)</li>'
        root_html = re.findall(root_pattern,htmls)
        re_name = r'<i class="nick" title="([\s\S]*?)">'
        re_number =r'<i class="js-num">([\s\S]*?)</i>'
        #re_title = r''
        alists = []
        for root in root_html:
            name = re.findall(re_name,root)
            number = re.findall(re_number,root)
            alist = {'name':name,'number':number}

            alists.append(alist)
            #print alists[0]
        return alists
    def print_html(self,lst):
        
        l = lambda lst:{'name':lst['name'][0].strip(),
        'number':lst['number'][0]
        } #python内置函数，去掉空格
        return map(l,lst) #map相当于遍历函数
    def rank_html(self,lst):
        lst = sorted(lst,key=self.send_rank,reverse=True) #根据number 倒序排序
        return lst
    
    def send_rank(self,lt):

        r = re.findall(r'\d*',lt['number'])

        number = float(r[0]) #抓换成整数
        if '万' in lt['number']:

            number *= 10000   
        return number


    def show_html(self,lst):
        for ls in range (0,len(lst)): 
            print ('rank:'+str(ls+1)
            +',name:'+lst[ls]['name']
            +',renqi:'+lst[ls]['number'])

if __name__ == "__main__":
    url = 'https://www.huya.com/g/lol'
    zb = zhibo()
    htmls = zb.html_url(url)
    #htmls = zb.html_url(url)
    lst = zb.html_parser(htmls)
    rank =  list(zb.print_html(lst))
    ls = zb.rank_html(rank)
    zb.show_html(ls)
