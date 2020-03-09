#coding:gbk
'''
程序：爬取b站中最受欢迎的程序课程
作者：徐佳梁
时间：2020年3月7日
'''
import requests
import bs4

def get_url(url,headers,params):

    re = requests.get(url,headers= headers,params = params)
    return re

def get_target(re,name):
    soup = bs4.BeautifulSoup(re.text,'html.parser')
    data = soup.find_all('div',class_= "headline clearfix")
    # print(data)

    with open(name+'的搜索结果.txt','a',encoding='utf-8') as f:
        for each in data:
            f.write(each.a['title']+'\n'+'http:'+each.a['href']+'\n')
    # for each in data:
    #     print(each.a['title'])
    #     print('http:'+each.a['href'])
def main():
    url = 'https://search.bilibili.com/all'#order:totalrank(综合排序),click,pubdate（最新发布）,dm,stow
    keyword = input('请输入搜索内容:')#keyword:搜索的关键词  #duration:时长选择：全部，10分钟，10-30,30-60，60以上 #tids_1=:0,1.....分区、分类
    page = input('请输入页数：') #page：搜索页数
    params = {'order': 'totalrank', 'duration': '4', 'tids_1': '0', 'page': '','keyword':''}
    params['keyword'] = keyword
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}

    for number in range(1,int(page)+1):
        params['page'] = number
        re = get_url(url,headers,params)
        get_target(re,name=keyword)
    # with open('re.txt','w',encoding='utf-8') as f:
    #     f.write(re.text)

if __name__ =='__main__':
    main()

