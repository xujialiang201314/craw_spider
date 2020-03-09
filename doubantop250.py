#coding:gbk
'''
������ȡ����top250��Ӱ��
���ߣ������
ʱ�䣺2020��3��1��
'''
import requests
from bs4 import BeautifulSoup
#��ȡ��Ӧ
def get_url(url,headers,proxies):
    html = requests.get(url, headers=headers, proxies=proxies)
    html = html.text
    return html
#��ȡÿ��ҳ���Ӱ����
def get_filmname(html):
    # a_name = []
    # title_name = []
    names = []
    soup = BeautifulSoup(html,'html.parser')
    data = soup.find_all('div',class_='hd')
    for each in data:
        # print(each.a.span.text)
        names.append(each.a.span.text)
    # print(names)
    return names
    # for a in data :
    #     if len(a)!=0:
    #         a_name.append(a)
    # for title in a_name:
    #     title2 = title.find_all(class_='title')
    #     if len(title2) != 0:
    #         title_name.append(title2)
    # for name in title_name:
    #     names.append(name[0].string)
    # return names
#������
def main():
    proxies = {'http': '218.75.158.153:3128',
               'http': '183.146.213.198:80'}  # proxiesҲ��һ���ֵ�����
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
    number = 0
    for num in range(0,250,25):
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        html= get_url(url, headers, proxies)
        names = get_filmname(html)
        for name in names:
            print(name)
            with open('����top250.txt', 'at') as f:
                f.write(str(number + 1) + '  ' + name + '\n')
            number += 1
if __name__ == '__main__':
    main()

# for num in range(0,250,25):
#     proxies = {'http': '218.75.158.153:3128',
#                'http': '183.146.213.198:80'}  # proxiesҲ��һ���ֵ�����
#     url = 'https://movie.douban.com/top250?start='+str(num)+'&filter='
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
#     html = requests.get(url,headers = headers,proxies = proxies)
#     html = html.text
#     # print(html)
#     soup = BeautifulSoup(html,'html.parser')
#     data = soup.find_all('li')
#     # print(data)
#     a_name = []
#     title_name = []
#     for a in data:
#         al = a.find_all('a')
#         if len(a) != 0:
#             a_name.append(a)
#     for title in a_name:
#         title2 = title.find_all(class_= 'title')
#         if len(title2) != 0:
#             title_name.append(title2)
#     # print(title_name)
#     names = []
#     for name in title_name:
#         names.append(name[0].string)
#     # print(names)
#     for name in names:
#         print(name)
#         with open('����top250.txt','at') as f:
#             f.write(str(number+1)+'  '+name+'\n')
#         number+=1

