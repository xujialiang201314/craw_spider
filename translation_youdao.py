'''
程序：用爬虫在有道翻译网站上爬取翻译
作者：徐佳梁
'''
import urllib.request
import urllib.parse
import json
import  random

content = input('请输入需要翻译的内容：')
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"  #获取url
#使用ip代理
# url = 'http://www.whatismyip.com.tw'
ip_list = ['183.146.213.198:80','218.75.158.153:3128']
my_ip = random.choice(ip_list)
print(my_ip)
proxy_support = urllib.request.ProxyHandler({'http':my_ip})
opener = urllib.request.build_opener(proxy_support)  #定制、创建一个opener
urllib.request.install_opener(opener)#安装opener  #调用opener
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
# print(html)
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

data={}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15815670001683'
data['sign'] = 'f640f91fa834dc00bbbd9f8ff33d02aa'
data['ts'] = '1581567000168'
data['bv'] = 'bbb3ed55971873051bc2ff740579bb49'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)  #发送请求，得到响应

html = response.read().decode('utf-8')   #读取数据
# print(html)
target = json.loads(html)              #保存数据
# print(target)
print('翻译结果为：%s '%(target['translateResult'][0][0]['tgt']))
# print(req.headers)