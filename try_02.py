import urllib.request
import re
import os
from multiprocessing.dummy import Pool
from time import perf_counter

def getHtml(url):   #根据url返回html网页
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('gbk')
        return html

def get_urllist(start_url): #给一个起始页，返回起始页里面的网址列表
    html = getHtml(start_url)
    url_list = []
    url_block = re.findall('<strong>正文</strong>(.*?)<td>&nbsp;</td>',html,re.S)[0]
    url_prvs = re.findall(' href="(.*?)">',url_block,re.S)
    for i in url_prvs:
        url_ok = start_url + i
        url_list.append(url_ok)
    return url_list

def get_article(html):  #在html中提取信息并返回
    chapter_name = re.search('size="4"> (.*?)</font>',html,re.S).group(1)
    text_block = re.search("<td width=\"820\" align=\"left\" bgcolor=\"#FFFFFF\">(.*?)</p>",html,re.S).group(1)
    text_block = text_block.replace('<p>','')
    text_block = text_block.replace('<br />','')
    return chapter_name,text_block

start_time = perf_counter() #开始计时
start_url = 'https://www.kanunu8.com/book3/6879/'
url_list = get_urllist(start_url)
os.makedirs('动物农场',exist_ok=True)   #判断文件夹是否存在

##for url in url_list:
##    html = getHtml(url)
##    chapter_name,text_block = get_article(html)
##    with open(os.path.join('动物农场',chapter_name + '.txt'),'w',encoding='utf-8') as f :
##        f.write(text_block)


def calc(url):  #定义一个操作函数
    html = getHtml(url)
    chapter_name,text_block = get_article(html)
    with open(os.path.join('动物农场',chapter_name + '.txt'),'w',encoding='utf-8') as f :
        f.write(text_block)
pool = Pool(3)
result = pool.map(calc,url_list)    #使用多线程操作

print("运行时间是: {:.5f}s".format(perf_counter()-start_time))

