#coding:gbk
'''
程序：爬取快代理里ip
作者：徐佳梁
时间：2020年3月1日
'''
import requests
from bs4 import BeautifulSoup
import time

#获取响应
def get_html(url,headers,proxies):
    re = requests.get(url, headers=headers, proxies=proxies)
    return re.text

#获取每一页的ip
def get_ip_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    data_tr = soup.find_all('tr')
    # print(data_tr)
    my_ip = []
    for tr in data_tr:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        data_title = []

        for td in ltd:
            data_title.append(td.string)
        my_ip.append(data_title)
       # print(my_ip)
    return my_ip

def printmy_iplist(num,my_ip):
    for i in range(num):
        u = my_ip[i]
        print('{:^15}{:^8}{:^8}'.format(u[0], u[1], u[3]))

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
    proxies = {'http': '218.75.158.153:3128',
               'http': '183.146.213.198:80'}  # proxies也是一个字典类型
    print('{:^15}{:^8}{:^8}'.format('ip', 'post', '类型'))
    for number in range(2,6,1):
        url = 'https://www.kuaidaili.com/free/inha/'+str(number)+'/'
        html = get_html(url,headers,proxies)
        my_ip = get_ip_list(html)
        # print(my_ip)
        printmy_iplist(15,my_ip)
        time.sleep(1)

if __name__=='__main__':

    main()

# for number in range(1,3,1):
#     print(number)
#     url = 'https://www.kuaidaili.com/free/inha/'+str(3) +'/'
#     re = requests.get(url,headers = headers,proxies = proxies)
#     html = re.text
#     # print(html)
#     soup = BeautifulSoup(html,'html.parser')
#     data_td = soup.find_all('td')
#     # print(data_td)
#     data_title = []
#     for td in data_td:
#         if len(td)!=0:
#             data_title.append(td)
#     my_ip = []
#     for title in data_title:
#         if len(title)!=0:
#             my_ip.append(title.string)
#     print(my_ip)
#     for num in range(0,99,7):
#         print(num)
#         # print(str(my_ip[num])+'  '+ str(my_ip[num+1] + '  ' + str(my_ip[num+3])))
#     print(my_ip[98])

