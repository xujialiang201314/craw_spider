#coding:gbk
'''
程序：从网站上下载（爬取）一张猫的图片
作者：徐佳梁
'''
# import urllib.request
#
# response = urllib.request.urlopen('http://placekitten.com/400/400')  #获取url，发送请求，并得到响应
# cat_img = response.read()          #提取数据
# # print(response.geturl())
# # print(response.info())
# # print(response.getcode())
# print(response)
# # print(type(response))
# with open('cat_400_400.jpg','wb') as f:    #保存数据
#     f.write(cat_img)

import requests
response = requests.get('http://placekitten.com/400/400')
# print(response.text)
# cat_img = response.read()
with open('cat_400_400_2.jpg','wb') as f:
    f.write(response.content)
